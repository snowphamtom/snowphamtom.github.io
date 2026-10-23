#!/usr/bin/env python3
"""Golden model + exhaustive stimulus generator for the V4 Sidon decoders.

Decoder semantics (the verified level100 / v3-spec classifier):
  syndrome s in Z^14, s = sum of signed columns (integer model, equal magnitude).
  s == 0            -> CLEAN   (class 0)
  s == +c_i / -c_i  -> REPAIR  (class 1, index=i, sign)
  s == +e_r / -e_r  -> TAIL    (class 2, index=r, sign)   [axis = tail edit]
  otherwise         -> REFUSE  (class 3)
Stimulus covers EVERY signed pattern of weight <= 3 plus zero and the tails:
  1 + 96 + 28 + 4512 + 138368 = 143005 vectors per matrix.
The generator asserts the refusal property while emitting: no pair or triple
syndrome may land on 0, a signed column, or a signed axis vector.
"""
import itertools, sys

MASKS_F64 = [263, 2059, 3855, 787, 5655, 15131, 10271, 6179, 4647, 13867,
             14895, 4403, 3895, 3899, 5951, 1347, 6215, 5707, 3407, 14931,
             13143, 6491, 5727, 3683, 15211, 11119, 15219, 14711, 15995,
             14975, 10371, 14727, 1419, 4751, 13971, 13207, 11163, 6563,
             935, 4779, 3759, 3507, 14011, 16063, 13251, 16071, 3791, 4563]

MASKS_GF128_CLOSED = [3302, 11338, 5994, 13323, 11967, 3170, 6306, 10885,
                      3996, 6803, 8405, 14156, 1167, 16122, 11103, 5680,
                      7829, 995, 1923, 1827, 7803, 2407, 4506, 7646, 4789,
                      7237, 14406, 14296, 4626, 3481, 12233, 8647, 9946,
                      14824, 5625, 13045, 9494, 11236, 9356, 12855, 3371,
                      2137, 2991, 2813, 6561, 3641, 5486, 4457]

R = 14
CLEAN, REPAIR, TAIL, REFUSE = 0, 1, 2, 3

def colvec(m):
    return tuple((m >> r) & 1 for r in range(R))

def build(masks, name, outpath):
    cols = [colvec(m) for m in masks]
    assert len(set(cols)) == 48 and all(any(c) for c in cols)
    assert not any(sum(c) == 1 for c in cols), "a column is an axis vector"
    colset = {}
    for i, c in enumerate(cols):
        colset[c] = (i, +1)
        colset[tuple(-x for x in c)] = (i, -1)
    axisset = {}
    for r in range(R):
        e = [0]*R; e[r] = 1
        axisset[tuple(e)] = (r, +1)
        axisset[tuple(-x for x in e)] = (r, -1)
    assert not (set(colset) & set(axisset)), "column/axis ambiguity"

    def syndrome(pattern):
        s = [0]*R
        for idx, sgn in pattern:
            c = cols[idx]
            for r in range(R):
                s[r] += sgn * c[r]
        return tuple(s)

    lines = []
    counts = {CLEAN: 0, REPAIR: 0, TAIL: 0, REFUSE: 0}

    def emit(pattern):
        # pattern: tuple of (col_idx, sign) with distinct idx, len 0..3
        if pattern:
            s = syndrome(pattern)
            if len(pattern) == 1:
                i, sgn = pattern[0]
                exp = (REPAIR, i, 1 if sgn > 0 else 0)
            else:
                assert s != (0,)*R, f"{name}: pattern -> zero syndrome"
                assert s not in colset, f"{name}: pattern aliases a column"
                assert s not in axisset, f"{name}: pattern aliases an axis"
                exp = (REFUSE, 0, 0)
        else:
            exp = (CLEAN, 0, 0)
        pat = 0
        slots = list(pattern) + [(63, 1)] * (3 - len(pattern))
        for k, (idx, sgn) in enumerate(slots):
            pat |= (idx | ((1 if sgn > 0 else 0) << 6)) << (7 * k)
        cls, eidx, esgn = exp
        expv = (cls << 7) | (eidx << 1) | esgn
        lines.append(f"{pat:06x} {expv:03x}")
        counts[cls] += 1

    def emit_tail(r, sgn):
        pat = 0
        slots = [(63, 1)] * 3
        for k, (idx, sg) in enumerate(slots):
            pat |= (idx | ((1 if sg > 0 else 0) << 6)) << (7 * k)
        # tails are driven on a dedicated TB input, encoded as pattern with
        # idx field 62 = 'tail slot' marker handled below; simpler: separate file
        expv = (TAIL << 7) | (r << 1) | (1 if sgn > 0 else 0)
        tail_lines.append(f"{r:02x} {(1 if sgn > 0 else 0):01x} {expv:03x}")
        counts[TAIL] += 1

    tail_lines = []
    emit(())                                            # zero pattern
    for i in range(48):                                 # singles, both signs
        for sgn in (+1, -1):
            emit(((i, sgn),))
    for i, j in itertools.combinations(range(48), 2):   # pairs, all 4 sign combos
        for si in (+1, -1):
            for sj in (+1, -1):
                emit(((i, si), (j, sj)))
    for i, j, k in itertools.combinations(range(48), 3):  # triples, all 8 combos
        for si in (+1, -1):
            for sj in (+1, -1):
                for sk in (+1, -1):
                    emit(((i, si), (j, sj), (k, sk)))
    for r in range(R):                                  # tails, both signs
        for sgn in (+1, -1):
            emit_tail(r, sgn)

    with open(outpath, "w") as f:
        f.write("\n".join(lines) + "\n")
    with open(outpath.replace(".hex", "_tails.hex"), "w") as f:
        f.write("\n".join(tail_lines) + "\n")
    total = sum(counts.values())
    print(f"{name}: {total} vectors  CLEAN={counts[CLEAN]} REPAIR={counts[REPAIR]} "
          f"TAIL={counts[TAIL]} REFUSE={counts[REFUSE]}")
    # emit the Verilog include: packed column table, mask47 in MSBs
    packed = 0
    for i, m in enumerate(masks):
        packed |= m << (14 * i)
    vh = outpath.replace("vectors/", "rtl/").replace("_vectors.hex", "_cols.vh")
    with open(vh, "w") as f:
        f.write(f"// {name}: 48 columns x 14 bits, column i at bits [14*i +: 14]\n")
        tag = "F64_COLS" if "f64" in outpath else "GF128_COLS"
        f.write(f"`define {tag} 672'h{packed:0168x}\n")
    print(f"  wrote {outpath} and {vh}")

build(MASKS_F64, "F64 spec set", "vectors/f64_vectors.hex")
build(MASKS_GF128_CLOSED, "GF128 fully-closed set", "vectors/gf128_vectors.hex")
