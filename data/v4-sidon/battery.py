#!/usr/bin/env python3
"""Exhaustive battery for the Sidon mask sets in this folder.
Loads every *_masks.csv in the current directory (columns: index,mask;
bit k of a mask is row k) and measures, in the unit-amplitude integer model:
  - distinctness / nonzero / row sums / column weights / min Hamming distance
  - XOR pair sums, integer pair sums (++), ordered differences (+-)
  - triple sums +++ and ++-: distinct counts, shared syndromes, cross-weight
    syndromes (a triple syndrome equal to a pair syndrome)
  - decoder acceptance of weight-3 patterns under three models:
      Model A  (admission classifier, as built in the HDL decoders):
               accept iff syndrome in {0} U {+-column} U {+-unit vector}
      Model A+ (amplitude-extended): also e*column and e*unit, e in {+-2,+-3}
      Model B  (pair-correcting lookup decoder): Model A plus pair syndromes
    A weight-3 pattern accepted under a model is a misrepair under that model.
Reproduces every figure in README.md. Python 3, standard library only."""
import csv, glob, itertools, os

def load(path):
    with open(path) as f:
        return [int(row["mask"]) for row in csv.DictReader(f)]

def analyze(name, masks):
    r = max(m.bit_length() for m in masks)
    cols = [tuple((m >> k) & 1 for k in range(r)) for m in masks]
    def add(*vs): return tuple(sum(x) for x in zip(*vs))
    def neg(v): return tuple(-x for x in v)
    def sub(a, b): return tuple(x - y for x, y in zip(a, b))
    def scale(e, v): return tuple(e * x for x in v)
    zero = tuple([0] * r)
    rowsums = [sum(c[k] for c in cols) for k in range(r)]
    weights = [sum(c) for c in cols]
    mind = min(sum(1 for a, b in zip(cols[i], cols[j]) if a != b)
               for i in range(48) for j in range(i + 1, 48))
    units = [tuple(1 if j == k else 0 for j in range(r)) for k in range(r)]
    A = {zero}
    for c in cols: A.add(c); A.add(neg(c))
    for e in units: A.add(e); A.add(neg(e))
    Aplus = set(A)
    for e_amp in (2, 3, -2, -3):
        for c in cols: Aplus.add(scale(e_amp, c))
        for e in units: Aplus.add(scale(e_amp, e))
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
    print(f"=== {name} (r={r}) ===")
    print(f"masks: count=48 distinct={len(set(masks)) == 48} nonzero={all(m != 0 for m in masks)}")
    print(f"row sums: {rowsums} total={sum(rowsums)}")
    print(f"column weights: min={min(weights)} max={max(weights)}; min Hamming distance={mind}")
    print(f"XOR pair sums distinct: {len(xor)}/1128")
    print(f"integer ++ distinct: {len(pp)}/1128; ordered +- distinct: {len(pm)}/2256")
    print(f"triples +++ distinct: {len(ppp)}/17296; ++- distinct: {len(ppm)}/51888")
    print(f"triple syndromes total distinct: {len(trip_syn)}/69184")
    print(f"+++ and ++- shared syndromes: {len(set(ppp) & set(ppm))}")
    print(f"triple syndromes equal to a pair syndrome: {len(trip_syn & pair_syn)}")
    print(f"weight-3 patterns accepted (misrepair): A={acc['A']} A+={acc['A+']} B={acc['B']} of 69184")
    print()

for path in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "*_masks.csv"))):
    analyze(os.path.basename(path).replace("_masks.csv", ""), load(path))
print("BATTERY DONE")
