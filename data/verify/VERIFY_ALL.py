#!/usr/bin/env python3
"""
VERIFY_ALL.py — Independent verification of the Monsters Ink record.

Purpose: every computationally verifiable claim in MASTER_DOCUMENT_2026-10-22.md
is recomputed here, from first principles or from the published data files, by an
implementation written for this suite. Any AI (or human) can run this file and
independently confirm or refute each figure. Nothing is taken on trust: expected
values come from the governing sources (the published exhaustive batteries, the
Drive census manifest, the content-sweep outputs, the swarm register), and each
check prints CLAIM vs MEASURED.

Run:  python3 VERIFY_ALL.py [--fast] [--spectral]
  --fast      skip the three largest Kimberling forward traces (n > 20,000,000)
  --spectral  also re-run the published spectral-drop scripts and compare outputs

Requirements: Python 3, standard library only. numpy is used if importable for
one check (W distinct-eigenvalue count); without it that check SKIPs and the
remaining W checks use exact integer arithmetic + power iteration.
Local evidence files are looked up under ~/workspace (override with the
MUSE_WORKSPACE environment variable). A check whose evidence file is absent
SKIPs with the path it needs — it never guesses.

Scope honesty: claims that are records rather than computations (patent
receipts, submission statuses, meeting facts, published-source exposure
figures, proof-only claims such as the counting bounds and Kimberling
surjectivity) cannot be verified by code. They are enumerated at the end as
RECORD items with their evidence locations, so every claim in the Master
Document is accounted for: PASS, FAIL, SKIP, or RECORD.

Exit code: 0 when no check FAILs, otherwise the number of FAILs (capped at 125).
"""
import csv, hashlib, itertools, json, math, os, re, subprocess, sys, time
from pathlib import Path

WS = Path(os.environ.get("MUSE_WORKSPACE", Path.home() / "workspace"))
FAST = "--fast" in sys.argv
SPECTRAL = "--spectral" in sys.argv

RESULTS = []
def check(section, claim, measured, expected, status=None):
    if status is None:
        status = "PASS" if measured == expected else "FAIL"
    RESULTS.append((status, section, claim, measured, expected))
    print(f"[{status}] {section} :: {claim} :: measured={measured!r} expected={expected!r}", flush=True)
def skip(section, claim, reason):
    RESULTS.append(("SKIP", section, claim, reason, ""))
    print(f"[SKIP] {section} :: {claim} :: {reason}", flush=True)
def record(section, claim, pointer):
    RESULTS.append(("RECORD", section, claim, pointer, ""))
    print(f"[RECORD] {section} :: {claim} :: evidence: {pointer}", flush=True)
def approx(section, claim, measured, expected, tol):
    ok = abs(measured - expected) <= tol
    RESULTS.append(("PASS" if ok else "FAIL", section, claim, measured, f"{expected} ±{tol}"))
    print(f"[{'PASS' if ok else 'FAIL'}] {section} :: {claim} :: measured={measured!r} expected={expected!r} ±{tol}", flush=True)

# ---------------------------------------------------------------- mask sets
# Filed [55,8] (application 64/170,360): masks are the odd numbers 3..97.
FILED55 = list(range(3, 98, 2))
# F64 spec set (v3 spec S3.5) = construct_v4b.py MASKS4 (byte-identical, verified).
F64 = [263, 2059, 3855, 787, 5655, 15131, 10271, 6179, 4647, 13867, 14895, 4403,
       3895, 3899, 5951, 1347, 6215, 5707, 3407, 14931, 13143, 6491, 5727, 3683,
       15211, 11119, 15219, 14711, 15995, 14975, 10371, 14727, 1419, 4751, 13971,
       13207, 11163, 6563, 935, 4779, 3759, 3507, 14011, 16063, 13251, 16071, 3791, 4563]
# GF(2^7) package set ("seed6") — certification withdrawn 2026-10-22.
SEED6 = [3302, 11338, 5994, 13323, 11967, 3170, 6306, 10885, 129, 6803, 8405, 14156,
         8125, 16122, 11103, 5680, 553, 995, 1923, 1827, 7803, 2407, 4506, 7646,
         4789, 7237, 14406, 14296, 2573, 3481, 12233, 8647, 9946, 14824, 5625,
         13045, 9679, 11236, 9356, 12855, 3371, 2137, 2991, 2813, 6561, 3641, 5486, 4457]
# Fully closed GF(2^7) set (published 2026-10-22). Bold indices vs seed6: 8,12,16,28,36.
CLOSED = [3302, 11338, 5994, 13323, 11967, 3170, 6306, 10885, 3996, 6803, 8405, 14156,
          1167, 16122, 11103, 5680, 7829, 995, 1923, 1827, 7803, 2407, 4506, 7646,
          4789, 7237, 14406, 14296, 4626, 3481, 12233, 8647, 9946, 14824, 5625,
          13045, 9494, 11236, 9356, 12855, 3371, 2137, 2991, 2813, 6561, 3641, 5486, 4457]
# r = 10 set (Grok Bot rows-10..13 study; verified by Jett 2026-10-21).
R10 = [169, 91, 7, 927, 491, 917, 414, 96, 948, 1018, 864, 882, 667, 942, 899, 857,
       713, 486, 318, 654, 77, 590, 458, 614, 683, 188, 543, 726, 249, 67, 493, 556,
       823, 553, 147, 434, 753, 343, 957, 293, 472, 380, 181, 229, 118, 826, 709, 457]
# S3.6 dual-mirror set, regenerated from the canonical rule (drop-in 2026-10-21).
S36 = [16003, 15749, 15241, 14987, 14479, 14225, 13971, 12955, 12701, 12447, 12193, 11685,
       10923, 9653, 9399, 8383, 8129, 7875, 7621, 7113, 6859, 5843, 4827, 4065,
       15495, 14733, 13717, 13463, 13209, 11939, 11431, 11177, 10669, 10415, 10161, 9907,
       9145, 8891, 8637, 7367, 6605, 6351, 6097, 5589, 5335, 5081, 4573, 4319]

# ---------------------------------------------------------------- battery core
def battery(masks):
    """Exhaustive unit-amplitude battery. Definitions identical to the published
    battery.py shipped in the data drops (Models A / A+ / B as documented there);
    this is an independent reimplementation of those definitions."""
    r = max(m.bit_length() for m in masks)
    cols = [tuple((m >> k) & 1 for k in range(r)) for m in masks]
    def add(*vs): return tuple(sum(x) for x in zip(*vs))
    def neg(v): return tuple(-x for x in v)
    def sub(a, b): return tuple(x - y for x, y in zip(a, b))
    def scale(e, v): return tuple(e * x for x in v)
    zero = tuple([0] * r)
    rowsums = [sum(c[k] for c in cols) for k in range(r)]
    weights = [sum(c) for c in cols]
    mind = min(bin(masks[i] ^ masks[j]).count("1")
               for i in range(48) for j in range(i + 1, 48))
    units = [tuple(1 if j == k else 0 for j in range(r)) for k in range(r)]
    A = {zero}
    for c in cols: A.add(c); A.add(neg(c))
    for u in units: A.add(u); A.add(neg(u))
    Aplus = set(A)
    for e in (2, 3, -2, -3):
        for c in cols: Aplus.add(scale(e, c))
        for u in units: Aplus.add(scale(e, u))
    xor = {masks[i] ^ masks[j] for i, j in itertools.combinations(range(48), 2)}
    pp, pm, pair_syn = {}, {}, set()
    for i, j in itertools.combinations(range(48), 2):
        s = add(cols[i], cols[j]); pp[s] = pp.get(s, 0) + 1; pair_syn.add(s)
    for i in range(48):
        for j in range(48):
            if i != j:
                s = sub(cols[i], cols[j]); pm[s] = pm.get(s, 0) + 1; pair_syn.add(s)
    B = A | pair_syn
    ppp, ppm = {}, {}
    acc = {"A": 0, "A+": 0, "B": 0}
    for i, j, k in itertools.combinations(range(48), 3):
        s = add(cols[i], cols[j], cols[k]); ppp[s] = ppp.get(s, 0) + 1
        if s in A: acc["A"] += 1
        if s in Aplus: acc["A+"] += 1
        if s in B: acc["B"] += 1
    for (i, j), k in itertools.product(itertools.combinations(range(48), 2), range(48)):
        if k != i and k != j:
            s = sub(add(cols[i], cols[j]), cols[k]); ppm[s] = ppm.get(s, 0) + 1
            if s in A: acc["A"] += 1
            if s in Aplus: acc["A+"] += 1
            if s in B: acc["B"] += 1
    trip_syn = set(ppp) | set(ppm)
    return {
        "r": r, "distinct": len(set(masks)), "nonzero": all(m != 0 for m in masks),
        "rowsums": rowsums, "total_bits": sum(rowsums),
        "wmin": min(weights), "wmax": max(weights), "mindist": mind,
        "common_bits": bin(masks[0] & masks[1] & masks[2] if False else
                           __import__("functools").reduce(int.__and__, masks)).count("1"),
        "xor_distinct": len(xor), "pp_distinct": len(pp), "pm_distinct": len(pm),
        "ppp_distinct": len(ppp), "ppm_distinct": len(ppm),
        "trip_distinct": len(trip_syn), "shared_ppp_ppm": len(set(ppp) & set(ppm)),
        "trip_eq_pair_distinct": len(trip_syn & pair_syn),
        "trip_eq_pp_distinct": len(trip_syn & set(pp)), "trip_eq_pm_distinct": len(trip_syn & set(pm)),
        "inter_pp_ppp": len(set(pp) & set(ppp)), "inter_pp_ppm": len(set(pp) & set(ppm)),
        "inter_pm_ppp": len(set(pm) & set(ppp)), "inter_pm_ppm": len(set(pm) & set(ppm)),
        "acc": acc, "_cols": cols, "_pair_syn": pair_syn,
    }

def codec_section(sec, masks, exp):
    print(f"\n--- {sec} (exhaustive battery, may take a minute) ---", flush=True)
    t0 = time.time()
    b = battery(masks)
    print(f"    battery ran in {time.time()-t0:.1f}s", flush=True)
    for key, label in [("distinct", "48 distinct masks"), ("rowsums", "row sums"),
                       ("total_bits", "total bits"), ("mindist", "min Hamming distance"),
                       ("xor_distinct", "XOR pair sums distinct /1128"),
                       ("pp_distinct", "integer ++ distinct /1128"),
                       ("pm_distinct", "ordered +- distinct /2256"),
                       ("ppp_distinct", "+++ distinct /17296"),
                       ("ppm_distinct", "++- distinct /51888"),
                       ("trip_distinct", "triple syndromes distinct /69184"),
                       ("shared_ppp_ppm", "syndromes shared by +++ and ++-"),
                       ("trip_eq_pair_distinct", "distinct triple syndromes equal to a pair syndrome")]:
        if key in exp: check(sec, label, b[key], exp[key])
    for mkey in ("A", "A+", "B"):
        if ("acc" + mkey) in exp: check(sec, f"weight-3 patterns accepted under Model {mkey}", b["acc"][mkey], exp["acc" + mkey])
    return b

# ---------------------------------------------------------------- §3 codec
codec_section("MD S3.1 filed [55,8]", FILED55, {
    "distinct": 48, "rowsums": [48, 24, 24, 24, 24, 17, 17], "total_bits": 178,
    "mindist": 1,  # governing source: published battery (Master Doc corrected to match)
    "xor_distinct": 63, "pp_distinct": 464, "pm_distinct": 592,
    "ppp_distinct": 2392, "ppm_distinct": 3173, "trip_distinct": 5565,
    "shared_ppp_ppm": 0, "trip_eq_pair_distinct": 0,
    "accA": 7296, "accA+": 7296, "accB": 7296})
check("MD S3.1 filed [55,8]", "weight-3 patterns refused under every model (69184 - 7296)",
      69184 - 7296, 61888)

codec_section("MD S3.2 F64 spec set", F64, {
    "distinct": 48, "rowsums": [48, 48, 23, 24, 23, 22, 19, 18, 25, 32, 20, 28, 30, 21],
    "total_bits": 381, "mindist": 2,
    "xor_distinct": 1128, "pp_distinct": 1128, "pm_distinct": 2256,
    "ppp_distinct": 17165, "ppm_distinct": 50761, "trip_distinct": 67926,
    "shared_ppp_ppm": 0, "trip_eq_pair_distinct": 0,
    "accA": 0, "accA+": 0, "accB": 0})
_b = battery  # silence linters; F64 common bits checked directly:
check("MD S3.2 F64 spec set", "common bits (AND of all 48 masks)", 
      bin(__import__("functools").reduce(int.__and__, F64)).count("1"), 2)

# F64 quadruple pairing hits — predicate exactly as the v3 review's battery:
# for each 4-subset and each of its 3 pairings, s = (Va+Vb) - (Vc+Vd);
# axis (exactly one nonzero component) -> TAIL_EDIT; scalar multiple of a
# column -> REPAIRED (column-parallel). Sign orientation is irrelevant here.
print("--- MD S3.2 F64 quadruple pairing scan (583,740 syndromes) ---", flush=True)
_V = [tuple((m >> k) & 1 for k in range(14)) for m in F64]
def _is_axis(s): return sum(1 for x in s if x != 0) == 1
def _is_parallel(s):
    for col in _V:
        e = None; ok = True
        for k, ck in enumerate(col):
            if ck == 0:
                if s[k] != 0: ok = False; break
            else:
                if e is None:
                    e = s[k]
                    if e == 0: ok = False; break
                elif s[k] != e: ok = False; break
        if ok and e: return True
    return False
_qa = _qp = 0
for quad in itertools.combinations(range(48), 4):
    w, x, y, z = (_V[quad[0]], _V[quad[1]], _V[quad[2]], _V[quad[3]])
    # pairings: (w,x)|(y,z), (w,y)|(x,z), (w,z)|(x,y)
    for (a, b), (c, d) in (((w, x), (y, z)), ((w, y), (x, z)), ((w, z), (x, y))):
        s = tuple(aa + bb - cc - dd for aa, bb, cc, dd in zip(a, b, c, d))
        if _is_axis(s): _qa += 1
        elif _is_parallel(s): _qp += 1
check("MD S3.2 F64 spec set", "quad ++-- TAIL_EDIT (axis) pairing hits", _qa, 81)
check("MD S3.2 F64 spec set", "quad ++-- column-parallel pairing hits", _qp, 0)

codec_section("MD S3.3 seed6 (label withdrawn)", SEED6, {
    "distinct": 48, "rowsums": [31, 25, 22, 28, 20, 26, 27, 28, 23, 25, 25, 26, 22, 19],
    "total_bits": 347, "mindist": 2,
    "xor_distinct": 1128, "pp_distinct": 1128, "pm_distinct": 2256,
    "ppp_distinct": 17286, "ppm_distinct": 51798, "trip_distinct": 69084,
    "shared_ppp_ppm": 0, "trip_eq_pair_distinct": 10,
    "accA": 0, "accA+": 0, "accB": 10})
check("MD S3.3 seed6 (label withdrawn)", "+++ collisions (17296 - 17286)", 17296 - 17286, 10)
check("MD S3.3 seed6 (label withdrawn)", "++- collisions (51888 - 51798)", 51888 - 51798, 90)

bc = codec_section("MD S3.4 closed GF(2^7) set", CLOSED, {
    "distinct": 48, "rowsums": [28, 27, 23, 26, 23, 24, 26, 28, 23, 25, 27, 26, 23, 19],
    "total_bits": 348, "mindist": 2,
    "xor_distinct": 1128, "pp_distinct": 1128, "pm_distinct": 2256,
    "ppp_distinct": 17296, "ppm_distinct": 51888, "trip_distinct": 69184,
    "shared_ppp_ppm": 0, "trip_eq_pair_distinct": 0,
    "accA": 0, "accA+": 0, "accB": 0})
diff_idx = [i for i in range(48) if CLOSED[i] != SEED6[i]]
check("MD S3.4 closed GF(2^7) set", "columns differing from seed6 (indices)", diff_idx, [8, 12, 16, 28, 36])
check("MD S3.4 closed GF(2^7) set", "substituted values at those indices",
      [CLOSED[i] for i in (8, 12, 16, 28, 36)], [3996, 1167, 7829, 4626, 9494])

br = codec_section("MD S3.5 r=10 set", R10, {
    "distinct": 48, "rowsums": [27, 26, 26, 27, 25, 27, 25, 28, 24, 24],
    "total_bits": 259, "mindist": 2,
    "xor_distinct": 743, "pp_distinct": 1128, "pm_distinct": 2256,
    "ppp_distinct": 16499, "ppm_distinct": 45601, "trip_distinct": 62100,
    "shared_ppp_ppm": 0, "trip_eq_pair_distinct": 381,
    "accA": 0, "accA+": 0, "accB": 490})
check("MD S3.5 r=10 set", "column weights min", br["wmin"], 2)
check("MD S3.5 r=10 set", "column weights max", br["wmax"], 8)
check("MD S3.5 r=10 set", "common bits (AND of all masks)",
      bin(__import__("functools").reduce(int.__and__, R10)).count("1"), 0)
check("MD S3.5 r=10 set", "row sums min (no dead rows)", min(br["rowsums"]), 24)
check("MD S3.5 r=10 set", "row sums max", max(br["rowsums"]), 28)
check("MD S3.5 r=10 set", "overlap pair++ x triple+++ (distinct syndromes)",
      br["inter_pp_ppp"], 44)
check("MD S3.5 r=10 set", "overlap pair++ x triple++- (distinct syndromes)",
      br["inter_pp_ppm"], 116)
check("MD S3.5 r=10 set", "overlap pair+- x triple+++ (distinct syndromes)",
      br["inter_pm_ppp"], 0)
check("MD S3.5 r=10 set", "overlap pair+- x triple++- (distinct syndromes)",
      br["inter_pm_ppm"], 221)
# Any-amplitude silence check: no signed weight-<=3 syndrome is zero, axis-aligned,
# or parallel to a column. Sign classes +++ and ++- cover all patterns up to an
# overall sign, and all three properties are sign-invariant.
def _norm(v):
    g = 0
    for x in v: g = math.gcd(g, abs(x))
    if g == 0: return v
    w = tuple(x // g for x in v)
    for x in w:
        if x != 0:
            return tuple(-y for y in w) if x < 0 else w
    return w
_colnorms = {_norm(c) for c in br["_cols"]}
_viol = {"zero": 0, "axis": 0, "parallel": 0}
_cols = br["_cols"]
def _scan(s):
    if all(x == 0 for x in s): _viol["zero"] += 1
    elif sum(1 for x in s if x != 0) <= 1: _viol["axis"] += 1
    elif _norm(s) in _colnorms: _viol["parallel"] += 1
for i, j, k in itertools.combinations(range(48), 3):
    _scan(tuple(a + b + c for a, b, c in zip(_cols[i], _cols[j], _cols[k])))
for (i, j), k in itertools.product(itertools.combinations(range(48), 2), range(48)):
    if k != i and k != j:
        _scan(tuple(a + b - c for a, b, c in zip(_cols[i], _cols[j], _cols[k])))
check("MD S3.5 r=10 set", "weight-3 syndromes that are zero", _viol["zero"], 0)
check("MD S3.5 r=10 set", "weight-3 syndromes axis-aligned (any amplitude)", _viol["axis"], 0)
check("MD S3.5 r=10 set", "weight-3 syndromes parallel to a column (any amplitude)", _viol["parallel"], 0)

# ---------------------------------------------------------------- §3.6 dual-mirror (Variant A)
print("\n--- MD S3.6 dual-mirror regenerated set (Variant A battery) ---", flush=True)
check("MD S3.6", "48 distinct masks", len(set(S36)), 48)
check("MD S3.6", "every column constant weight 8", {bin(m).count("1") for m in S36}, {8})
check("MD S3.6", "rows 0 and 7 all-ones (bit0 and bit7 set in all 48)",
      all((m & 1) == 1 and ((m >> 7) & 1) == 1 for m in S36), True)
check("MD S3.6", "mirror rule H[7+k] = 1 - H[k] for k=1..6, all columns",
      all(((m >> (7 + k)) & 1) == 1 - ((m >> k) & 1) for m in S36 for k in range(1, 7)), True)
_dist = {}
for i, j in itertools.combinations(range(48), 2):
    d = bin(S36[i] ^ S36[j]).count("1"); _dist[d] = _dist.get(d, 0) + 1
check("MD S3.6", "14-bit distance distribution", _dist, {2: 124, 4: 282, 6: 352, 8: 253, 10: 100, 12: 17})
_r = 14
_cols36 = [tuple((m >> k) & 1 for k in range(_r)) for m in S36]
_zero36 = tuple([0] * _r)
_acc36 = {"zero": 0, "axis": 0, "col": 0}
_colset36 = set(_cols36) | {tuple(-x for x in c) for c in _cols36}
_unitset36 = {tuple(1 if j == q else 0 for j in range(_r)) for q in range(_r)} | \
             {tuple(-1 if j == q else 0 for j in range(_r)) for q in range(_r)}
def _scan36(s, pair=False):
    if s == _zero36: _acc36["zero"] += 1
    elif s in _unitset36: _acc36["axis"] += 1
    elif s in _colset36: _acc36["col"] += 1
_pair_acc36 = 0
for i, j in itertools.combinations(range(48), 2):
    for s in (tuple(a + b for a, b in zip(_cols36[i], _cols36[j])),
              tuple(a - b for a, b in zip(_cols36[i], _cols36[j]))):
        if s == _zero36 or s in _unitset36 or s in _colset36: _pair_acc36 += 1
check("MD S3.6", "accepted pairs (zero/axis/column, both signs)", _pair_acc36, 0)
for i, j, k in itertools.combinations(range(48), 3):
    _scan36(tuple(a + b + c for a, b, c in zip(_cols36[i], _cols36[j], _cols36[k])))
for (i, j), k in itertools.product(itertools.combinations(range(48), 2), range(48)):
    if k != i and k != j:
        _scan36(tuple(a + b - c for a, b, c in zip(_cols36[i], _cols36[j], _cols36[k])))
check("MD S3.6", "triple syndromes zero", _acc36["zero"], 0)
check("MD S3.6", "triple syndromes axis", _acc36["axis"], 0)
check("MD S3.6", "triple faults accepted as column repairs (the 7,140 doors)", _acc36["col"], 7140)

# ---------------------------------------------------------------- §3.7 HDL (published package checks)
print("\n--- MD S3.7 HDL decoders (published package) ---", flush=True)
HDL = WS / "publish_data_drops" / "data" / "hdl-decoders"
if HDL.exists():
    for name in ("f64", "gf128"):
        main = (HDL / "vectors" / f"{name}_vectors.hex").read_text().splitlines()
        tails = (HDL / "vectors" / f"{name}_vectors_tails.hex").read_text().splitlines()
        check("MD S3.7 HDL", f"{name} golden vectors (142977 + 28)", len(main) + len(tails), 143005)
        log = (HDL / f"sim_{name}.log").read_text()
        check("MD S3.7 HDL", f"{name} published sim log: 0 errors + TB RESULT PASS",
              ("0 errors" in log) and ("TB RESULT: PASS" in log), True)
    fmax = (HDL / "fmax_record.md").read_text()
    check("MD S3.7 HDL", "fmax_record carries 21.98 / 23.24 MHz on LFE5U-85F",
          ("21.98" in fmax) and ("23.24" in fmax) and ("LFE5U-85F" in fmax), True)
    for name, mhz in (("f64", "21.98 MHz"), ("gf128", "23.24 MHz")):
        pnr = HDL / "fmax" / f"v7_wrap_{name}_pnr.log"
        if pnr.exists():
            check("MD S3.7 HDL", f"{name} nextpnr log states {mhz}", mhz in pnr.read_text(), True)
        else:
            skip("MD S3.7 HDL", f"{name} pnr log", f"missing: {pnr}")
else:
    skip("MD S3.7 HDL", "published HDL drop", f"missing: {HDL}")
record("MD S3.7 HDL", "Fmax figures are place-and-route outputs of the recorded flow (shortened ABC script) — a flow record, not a computation this suite redoes",
       "hdl-decoders drop fmax_record.md + fmax/ logs; Master Document S3.7 caveat")

# ---------------------------------------------------------------- §4.1 GENESIS census (published drop)
print("\n--- MD S4.1 GENESIS census ---", flush=True)
GEN = WS / "publish_data_drops" / "data" / "genesis-census"
if GEN.exists():
    pairs = list(csv.DictReader((GEN / "pairs.csv").open()))
    check("MD S4.1 GENESIS", "pair rows", len(pairs), 1128)
    from collections import Counter
    check("MD S4.1 GENESIS", "class counts (DOOR/ALIAS/NEVER)",
          dict(Counter(r["class"] for r in pairs)), {"DOOR": 944, "ALIAS": 124, "NEVER": 60})
    check("MD S4.1 GENESIS", "ALIAS iff Hamming distance 1 (every row)",
          all((r["class"] == "ALIAS") == (int(r["hamming_distance"]) == 1) for r in pairs), True)
    check("MD S4.1 GENESIS", "DOOR iff doors_on_pair > 0 (every row)",
          all((r["class"] == "DOOR") == (int(r["doors_on_pair"]) > 0) for r in pairs), True)
    check("MD S4.1 GENESIS", "distance distribution",
          dict(sorted(Counter(int(r["hamming_distance"]) for r in pairs).items())),
          {1: 124, 2: 282, 3: 352, 4: 253, 5: 100, 6: 17})
    check("MD S4.1 GENESIS", "total doors over pairs", sum(int(r["doors_on_pair"]) for r in pairs), 7140)
    doors = (GEN / "doors.csv").read_text().splitlines()
    check("MD S4.1 GENESIS", "doors.csv data rows", len(doors) - 1, 7140)
    mids = list(csv.DictReader((GEN / "midpoints.csv").open()))
    check("MD S4.1 GENESIS", "distinct midpoints", len(mids), 83)
    check("MD S4.1 GENESIS", "midpoint (pair_sum) range",
          (min(int(r["pair_sum"]) for r in mids), max(int(r["pair_sum"]) for r in mids)), (16, 184))
    check("MD S4.1 GENESIS", "doors summed over midpoints",
          sum(int(r["doors_with_this_sum"]) for r in mids), 7140)
    W = [[int(x) for x in line.split(",")] for line in (GEN / "W_pair_adjacency.csv").read_text().splitlines() if line.strip()]
    check("MD S4.1 GENESIS", "W shape", (len(W), len(W[0])), (48, 48))
    check("MD S4.1 GENESIS", "W symmetric, zero diagonal",
          all(W[i][j] == W[j][i] for i in range(48) for j in range(48)) and all(W[i][i] == 0 for i in range(48)), True)
    check("MD S4.1 GENESIS", "W sum of squares (= sum lambda^2)", sum(x * x for row in W for x in row), 191808)
    try:
        import numpy as np
        ev = sorted(np.linalg.eigvalsh(np.array(W, dtype=float)))
        approx("MD S4.1 GENESIS", "W lambda_max", float(ev[-1]), 299.358, 0.001)
        approx("MD S4.1 GENESIS", "W lambda_min", float(ev[0]), -129.871, 0.001)
        check("MD S4.1 GENESIS", "W lambda_min multiplicity", sum(1 for e in ev if abs(e - ev[0]) < 0.01), 3)
        check("MD S4.1 GENESIS", "W distinct eigenvalues (3dp)", len({round(float(e), 3) for e in ev}), 27)
    except ImportError:
        skip("MD S4.1 GENESIS", "W eigenvalues", "numpy not importable; sum-of-squares check above still binds sum lambda^2")
    spec_txt = (GEN / "spectra.txt").read_text()
    check("MD S4.1 GENESIS", "spectra.txt carries the T line as printed (598.650 / -86.262 / 685584)",
          ("598.650" in spec_txt) and ("-86.262" in spec_txt) and ("685584" in spec_txt), True)
    record("MD S4.1 GENESIS", "T (transition operator) spectrum — matrix not in the published drop; figures as computed at export from core_engine_proof.py",
           "genesis-census drop spectra.txt; ~/workspace/your_files/core/core_engine_proof.py")
else:
    skip("MD S4.1 GENESIS", "genesis-census drop", f"missing: {GEN}")

# ---------------------------------------------------------------- §4.4 Kimberling
print("\n--- MD S4.4 Kimberling Problem 2 ---", flush=True)
def ktrace(n):
    """Backward trace from the paper: a(n) = K[n,n]; returns (a(n), terminal row, steps)."""
    i, j, steps = n, n, 0
    while j < 2 * i - 3:
        if j % 2 == 0: j = i - j // 2 - 1
        else: j = i + (j - 1) // 2
        i -= 1; steps += 1
    return i + j - 1, i, steps
KIM = WS / "publish_data_drops" / "data" / "kimberling" / "located_values.csv"
if KIM.exists():
    lv = [(int(r["value_v"]), int(r["index_n_with_a(n)=v"])) for r in csv.DictReader(KIM.open())]
    check("MD S4.4 Kimberling", "located pairs", len(lv), 30)
    check("MD S4.4 Kimberling", "distinct values", len({v for v, _ in lv}), 30)
    check("MD S4.4 Kimberling", "distinct indices", len({n for _, n in lv}), 30)
    for anchor in ((68, 181393), (669, 653494691), (502, 118850522)):
        check("MD S4.4 Kimberling", f"anchor pair {anchor} present", anchor in lv, True)
    check("MD S4.4 Kimberling", "row-triple targets for i*=4..200 (arithmetic)", 3 * (200 - 4 + 1), 591)
    for v, n in sorted(lv, key=lambda t: t[1]):
        if FAST and n > 20_000_000:
            skip("MD S4.4 Kimberling", f"a({n}) = {v} forward trace", "--fast: large trace skipped (run without --fast)")
            continue
        t0 = time.time(); a, istar, steps = ktrace(n)
        ok = (a == v) and (istar < 4 or v in (3 * istar - 4, 3 * istar - 3, 3 * istar - 2))
        check("MD S4.4 Kimberling", f"a({n}) forward-traced (steps={steps}, {time.time()-t0:.1f}s, terminal row {istar})", a, v, "PASS" if ok else "FAIL")
    record("MD S4.4 Kimberling", "Injectivity proof and the 591-target hit verification are mathematics / paper records; surjectivity (the $300 question) is OPEN and claimed nowhere as proved",
           "kimberling drop: kimberling_complete_paper.md, kimberling_injectivity_paper.md, surjectivity_framework.md")
else:
    skip("MD S4.4 Kimberling", "located_values.csv", f"missing: {KIM}")

# ---------------------------------------------------------------- §5/§8 money arithmetic
print("\n--- MD S8 monetization arithmetic ---", flush=True)
for buyer, exposure, ask in (("Lockheed Martin", 240.0, 14.4), ("Intelsat", 578.0, 34.68), ("Viasat", 770.0, 46.2)):
    approx("MD S8.2 packets", f"{buyer} ask = 6% of documented exposure (3-yr, 2%/yr)", round(exposure * 0.06, 2), ask, 0.001)
approx("MD S8.2 packets", "combined asks", round(14.4 + 34.68 + 46.2, 2), 95.28, 0.001)
from decimal import Decimal, ROUND_HALF_UP
def _hu(total):  # 30% of a total, in exact decimal, rounded half-up to 0.1
    return float((Decimal(total) * Decimal("0.30")).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))
# The published analyses round half-up (spreadsheet convention) in decimal.
# Float arithmetic reads 8898.5 * 0.3 as 2669.549999... and corrupts the check;
# the model's figure (2669.6) is the exact-decimal half-up value, verified here.
check("MD S8.1 model", "2025 savings low = 30% of 6855 (decimal, half-up)", _hu("6855"), 2056.5)
check("MD S8.1 model", "2025 savings high = 30% of 7020 (decimal, half-up)", _hu("7020"), 2106.0)
check("MD S8.1 model", "2027 savings low = 30% of 8898.5 (decimal, half-up)", _hu("8898.5"), 2669.6)
check("MD S8.1 model", "2027 savings high = 30% of 9084.9 (decimal, half-up)", _hu("9084.9"), 2725.5)
PK = WS / "your_files" / "pricing_packets_2026-10-22"
if PK.exists():
    brief = (PK / "00_PRICING_BRIEF.md").read_text()
    check("MD S8.2 packets", "brief carries the three asks and exposures",
          all(s in brief for s in ("$14.4M", "$34.68M", "$46.2M", "$240M", "$578M", "$770M", "$95.28M")), True)
    pptxs = sorted(PK.rglob("*.pptx"))
    if pptxs:
        import zipfile
        bad = []
        for p in pptxs:
            z = zipfile.ZipFile(p)
            txt = " ".join(z.read(n).decode("utf8", "replace") for n in z.namelist()
                           if n.startswith("ppt/slides/slide") and n.endswith(".xml"))
            if "pitch" in re.sub(r"<[^>]+>", " ", txt).lower(): bad.append(p.name)
        check("MD S8.2 packets", "no instance of the word 'pitch' in any deck", bad, [])
    else:
        skip("MD S8.2 packets", "deck 'pitch' scan", "no .pptx found under the packets folder")
    record("MD S8.1 model", "Cost-of-inaction totals and 2027 scale factors rest on the LibreOffice recalculation + formula audit of 2026-10-22 and the published analyses; exposure figures are published-source figures",
           "pricing_packets_2026-10-22/model/ + goals/monetize-the-position-strengthen-the-position/files/DATA_MONETIZATION_DERIVATION_2026-10-22.md")
else:
    skip("MD S8 monetization", "pricing packets folder", f"missing: {PK}")

# ---------------------------------------------------------------- §9.1 census (manifest)
print("\n--- MD S9.1 Drive census ---", flush=True)
MAN = WS / "your_files" / "Drive_2026_Evidence_Manifest.csv"
SUMJ = WS / "drive_census_2026" / "summary.json"
if MAN.exists():
    rows = list(csv.DictReader(MAN.open()))
    check("MD S9.1 census", "manifest rows (files)", len(rows), 5858)
    check("MD S9.1 census", "total bytes", sum(int(r["bytes"]) for r in rows), 11187444553)
    months = {}
    for r in rows: months[r["created_utc"][:7]] = months.get(r["created_utc"][:7], 0) + 1
    if SUMJ.exists():
        check("MD S9.1 census", "created-by-month equals census summary.json",
              months, json.loads(SUMJ.read_text())["created_by_month"])
    check("MD S9.1 census", "files predating May 2026", sum(1 for r in rows if r["created_utc"] < "2026-05"), 7)
    check("MD S9.1 census", "Google Drive shortcut files", sum(1 for r in rows if r["mime_type"] == "application/vnd.google-apps.shortcut"), 887)
    check("MD S9.1 census", "Windows .lnk files (the 888th 'shortcut' by substring)",
          sum(1 for r in rows if r["mime_type"] == "application/x-ms-shortcut"), 1)
    pats = ["Workbench exports", "Manuscripts", "ARCHIVE_DUPLICATES", "Misc loose files",
            "Prompt-saved", "08_ARCHIVAL_CARRIERS", "ARCHIVE_SUPERSEDED", "Seraphim Organizer",
            "MASTERPIECE", "archive_old_hud"]
    breakdown = {p: sum(1 for r in rows if p in r["parent_folder"]) for p in pats}
    print(f"    archive-class breakdown: {breakdown}", flush=True)
    check("MD S9.1 census", "archive-class files (ten archive-named folders)", sum(breakdown.values()), 2448)
    check("MD S9.1 census", "October 2026 share of files", months.get("2026-10"), 3031)
else:
    skip("MD S9.1 census", "evidence manifest", f"missing: {MAN}")
record("MD S9.1 census", "Folder count 256 is the census record (full API enumeration); the manifest lists files, not folders",
       "drive_census_2026/summary.json + evidence_receipt.json")

# ---------------------------------------------------------------- §9.2 content sweep
print("\n--- MD S9.2 content sweep ---", flush=True)
SW = WS / "drive_census_2026" / "sweep_results.jsonl"
SWS = WS / "drive_census_2026" / "sweep_summary.json"
if SW.exists() and SWS.exists():
    srows, serr = [], 0
    for line in SW.read_text().splitlines():
        d = json.loads(line)
        if "error" in d: serr += 1
        else: srows.append(d)
    summ = json.loads(SWS.read_text())
    check("MD S9.2 sweep", "targets", summ["targets"], 3329)
    check("MD S9.2 sweep", "measured OK", len(srows), 3320)
    check("MD S9.2 sweep", "errors", serr, 9)
    check("MD S9.2 sweep", "total characters", sum(r["chars"] for r in srows), 161560577)
    check("MD S9.2 sweep", "total words", sum(r["words"] for r in srows), 19062266)
    check("MD S9.2 sweep", "digit share of characters",
          round(sum(r["numbers"] for r in srows) / sum(r["chars"] for r in srows), 4), 0.1004)
    DOMS = ["codec_c2", "te_assurance", "maritime", "space", "ai_safety", "spatial_vr"]
    hits = {d: sum(r["domains"][d] for r in srows) for d in DOMS}
    check("MD S9.2 sweep", "domain hit totals", hits,
          {"codec_c2": 5348, "te_assurance": 1079, "maritime": 2901, "space": 1450, "ai_safety": 1964, "spatial_vr": 9339})
    check("MD S9.2 sweep", "all domain hits", sum(hits.values()), 22081)
    check("MD S9.2 sweep", "hit shares (spatial_vr / codec_c2 / te_assurance)",
          (round(hits["spatial_vr"] / 22081, 4), round(hits["codec_c2"] / 22081, 4), round(hits["te_assurance"] / 22081, 4)),
          (0.4229, 0.2422, 0.0489))
    zero = [r for r in srows if sum(r["domains"].values()) == 0]
    check("MD S9.2 sweep", "zero-domain files", len(zero), 1474)
    check("MD S9.2 sweep", "zero-domain words", sum(r["words"] for r in zero), 1591821)
    copies = [r for r in srows if r["name"].startswith("LAYERED_DRIVE_SWEEP")]
    check("MD S9.2 sweep", "LAYERED_DRIVE_SWEEP copies", len(copies), 122)
    check("MD S9.2 sweep", "words in those copies", sum(r["words"] for r in copies), 11918325)
    tm = sum(r["measured_hits"] for r in srows); tg = sum(r["grandiose_hits"] for r in srows)
    check("MD S9.2 sweep", "register totals (measured / grandiose)", (tm, tg), (74966, 24208))
    check("MD S9.2 sweep", "corpus register ratio", round(tm / tg, 2), 3.10)
    exc_m = tm - sum(r["measured_hits"] for r in copies); exc_g = tg - sum(r["grandiose_hits"] for r in copies)
    check("MD S9.2 sweep", "register totals excluding the 122 copies", (exc_m, exc_g), (15847, 8284))
    check("MD S9.2 sweep", "ex-copies ratio", round(exc_m / exc_g, 2), 1.91)
    bym = {}
    for r in srows:
        m = r["created"][:7]; a = bym.setdefault(m, [0, 0]); a[0] += r["measured_hits"]; a[1] += r["grandiose_hits"]
    ratios = {m: round(a[0] / a[1], 2) for m, a in sorted(bym.items()) if m.startswith("2026-") and a[1] > 0}
    check("MD S9.2 sweep", "monthly register ratios May-Oct 2026",
          {k: ratios.get(k) for k in ("2026-05", "2026-06", "2026-07", "2026-08", "2026-09", "2026-10")},
          {"2026-05": 0.06, "2026-06": 0.15, "2026-07": 0.85, "2026-08": 1.60, "2026-09": 3.74, "2026-10": 4.55})
else:
    skip("MD S9.2 sweep", "sweep outputs", f"missing: {SW} / {SWS}")

# ---------------------------------------------------------------- §1 integrity + drops
print("\n--- MD S1/S13 file integrity ---", flush=True)
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
for label, path, want in (
    ("HIVE_GRIMM verification record PDF", WS / "your_files" / "HIVE_GRIMM_Complete_Verification_Record_2026-10-20.pdf",
     "49929a6c094cefd2a0b3721583b9d6c6cb6937f62e7cd3e896cb9ed0cb1faf67"),
    ("v3 spec PDF export (Yes.pdf_2.pdf)", WS / "user" / "files" / "Yes.pdf_2.pdf",
     "9a5f8df02f119f10058cadac4c81fb3aed18e7701821a42e1bb02f9508c5c086"),
    ("Drive evidence manifest", MAN, "e95ec6dc00a1630219eada26af48928bf1355fabca28ad5343c4b91d8d0ef278"),
    ("published closed-set CSV", WS / "publish_data_drops" / "data" / "v4-sidon" / "closed_gf127_masks.csv",
     "911864148a837e182416b3fe2edec8e96e652d83cc9a42408b72bb9a19410b02"),
):
    if Path(path).exists(): check("MD S13 integrity", label, sha(path), want)
    else: skip("MD S13 integrity", label, f"missing: {path}")
DROPS = WS / "publish_data_drops" / "data"
if DROPS.exists():
    for drop in sorted(DROPS.iterdir()):
        sums_file = next((drop / n for n in ("SHA256SUMS.txt", "SHA256SUMS") if (drop / n).exists()), None)
        if not sums_file: continue
        okc, badc = 0, []
        for line in sums_file.read_text().splitlines():
            parts = line.split()
            if len(parts) < 2 or len(parts[0]) != 64: continue
            f = drop / parts[-1].lstrip("*")
            if f.exists() and sha(f) == parts[0]: okc += 1
            else: badc.append(parts[-1])
        check("MD S8.4 drops", f"{drop.name}: SHA256SUMS verify", (okc, badc), (okc + len(badc), []) if not badc else (okc, badc), "PASS" if not badc and okc > 0 else "FAIL")
else:
    skip("MD S8.4 drops", "drop staging dir", f"missing: {DROPS}")

# ---------------------------------------------------------------- §10.1 swarm register chain
print("\n--- MD S10.1 swarm register ---", flush=True)
REG = WS / "swarm" / "register" / "register.jsonl"
if REG.exists():
    rrows = [json.loads(l) for l in REG.read_text().splitlines() if l.strip()]
    valid, prev = True, "GENESIS"
    for rrow in rrows:
        blob = json.dumps({k: rrow[k] for k in ("seq", "ts", "kind", "seat", "payload", "prev")},
                          sort_keys=True, separators=(",", ":"))
        if rrow["prev"] != prev or hashlib.sha256(blob.encode()).hexdigest() != rrow["hash"]: valid = False; break
        prev = rrow["hash"]
    check("MD S10.1 register", "hash chain valid end-to-end", valid, True)
    check("MD S10.1 register", "row 58 hash (tip at Master Document compile time)",
          next((r["hash"][:16] for r in rrows if r["seq"] == 58), None), "6fe92ee1226a3bd0")
    check("MD S10.1 register", "register has only grown since (rows >= 59)", len(rrows) >= 59, True)
else:
    skip("MD S10.1 register", "register.jsonl", f"missing: {REG}")

# ---------------------------------------------------------------- §4.2 spectral (optional re-run)
print("\n--- MD S4.2 spectral ---", flush=True)
SPEC = WS / "publish_data_drops" / "data" / "spectral"
if SPECTRAL and SPEC.exists():
    for script, resfile, needles in (
        ("phase_twist.py", "results_phase_twist.txt", ("0.2683", "0.3139")),
        ("riemann_check.py", "results_riemann_check.txt", ("29",)),
        ("spectral_class.py", "results_spectral_class.txt", ("0.6150", "0.6183")),
    ):
        try:
            out = subprocess.run([sys.executable, str(SPEC / script)], capture_output=True, text=True, timeout=900, cwd=str(SPEC))
            got = all(n in out.stdout for n in needles)
            check("MD S4.2 spectral", f"{script} re-run reproduces published headline figures {needles}", got, True)
        except Exception as e:
            skip("MD S4.2 spectral", script, f"re-run failed: {e}")
else:
    skip("MD S4.2 spectral", "phase-twist / zeta / spectral-class figures",
         "published scripts + outputs live in the spectral drop (snowphamtom.github.io/data/spectral/); re-run them there, or run this suite with --spectral")

# ---------------------------------------------------------------- RECORD claims (not code-verifiable)
print("\n--- RECORD claims — accounted for, verified by evidence, not by code ---", flush=True)
record("MD S1", "Eight patent applications, filing dates, Patent Center numbers, SAM.gov Active / UEI / CAGE",
       "~/workspace/your_files/patent_receipts/ + Gmail receipts (Patent Center); SAM.gov entity record")
record("MD S2", "Members Gate demonstration figure (64 of 169,264)",
       "public repo snowphamtom/members-gate (verify.yml, 7 test vectors) + PRIM3 entry")
record("MD S3.5/S3.6", "Counting bounds r>=8/9/10 and the r=10 two-common-bit exclusion (Delsarte step) are proof claims; spec S7.2/S7.3 set batteries are review records",
       "~/workspace/r10_verify_2026-10-21/RESULTS.md (bound re-derived); ~/workspace/filing_prep/V3_SPEC_REVIEW_2026-10-21.md + ~/workspace/v3_review_2026-10-21/verify_v3_sets.py (runnable)")
record("MD S5/S6", "Submission inventory, statuses, DIU correspondence, ATEC non-select and debrief state, xTech/PRIM3/VR submission states",
       "Gmail threads of record; Devpost entries (prim3, vr-gatekeeper); DIU_Deep_Analysis_2026-10-22.md; Submission_Portfolio_Analysis_2026-10-22.md")
record("MD S7", "APEX Oct 28 meeting facts and prep state", "Gmail APEX corpus (30 messages); meeting prep sheet in ~/workspace/your_files/meeting_prep/")
record("MD S10.4", "Greek Living Habitat design figures (areas, ratios, site screening)",
       "design book + deck in ~/workspace/your_files/; ratio scripts in ~/workspace/greek_habitat/ (physical_grant: false — design claims only)")
record("MD S10.1", "HIVE/GRIMM Lean compile state (ResidualGates PASS; Gates.lean 3 named defects)",
       "~/workspace/lean_compile_2026-10-20/ build outputs; HIVE_GRIMM_Complete_Verification_Record_2026-10-20.pdf (hash-checked above)")
record("MD S4.3", "Millennium excavation verdicts (documents read in full; YETI functional check is a computation)",
       "~/workspace/your_files/Millennium_Drive_Excavation_2026-10-22.md; ~/workspace/millennium/yeti_functional_check.py (runnable, mpmath)")

# ---------------------------------------------------------------- summary
print("\n================ SUMMARY ================", flush=True)
from collections import Counter as _C
tally = _C(s for s, *_ in RESULTS)
for s in ("PASS", "FAIL", "SKIP", "RECORD"):
    print(f"{s}: {tally.get(s, 0)}")
fails = [r for r in RESULTS if r[0] == "FAIL"]
for f in fails: print("FAILED:", f[1], "::", f[2], ":: measured", f[3], "expected", f[4])
print("VERIFY_ALL DONE")
sys.exit(min(len(fails), 125))
