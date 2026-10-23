#!/usr/bin/env python3
"""LABEL-FREE SPECTRAL TEST. Question: which universality class do the spectra
in Taylor's corpus actually sit in, measured against the zeta zeros and against
seeded random-matrix controls? Statistic: the r-ratio <r> (Atas et al. 2013) -
unfolding-free. Reference: Poisson 0.3863, GOE 0.5359, GUE 0.6027.
Zeros are GUE-class (Montgomery-Odlyzko). Data decides; no labels pre-applied."""
import csv, io, runpy, sys
import numpy as np
import mpmath as mp
from contextlib import redirect_stdout

def rratio(eigs):
    e = np.sort(np.asarray(eigs, dtype=float))
    s = np.diff(e)
    if len(s) < 2: return float('nan'), len(e), 0.0
    r = np.minimum(s[:-1], s[1:]) / np.maximum(s[:-1], s[1:])
    return float(np.mean(r)), len(e), float(np.mean(s == 0))

rng = np.random.default_rng(20261022)
def goe(n):
    A = rng.standard_normal((n, n)); return np.linalg.eigvalsh((A + A.T) / 2)
def gue(n):
    A = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    return np.linalg.eigvalsh((A + A.conj().T) / 2)
def poi(n):
    return np.sort(rng.uniform(0, n, n))

for name, gen, n, trials in (("GOE control", goe, 48, 300), ("GUE control", gue, 48, 300),
                             ("Poisson control", poi, 48, 300)):
    rs = [rratio(gen(n))[0] for _ in range(trials)]
    print(f"{name:>16}: <r> = {np.mean(rs):.4f} +- {np.std(rs):.4f}  (n={n}, {trials} trials)")

# --- H14 syndrome matrix (his CSV) ---
H = np.loadtxt("/home/hatch/workspace/your_files/core/H14_syndrome_48x48.csv", delimiter=",")
evH = np.linalg.eigvalsh(H)
nz = evH[np.abs(evH) > 1e-8]
print(f"\nH14 syndrome: rank {np.linalg.matrix_rank(H)}, nonzero eigenvalues {len(nz)} of 48 "
      f"-> spacing statistics undefined on 41-fold degenerate zero; distinct nonzero eigs: {np.round(np.sort(nz),3)}")

# --- W: his pair-adjacency operator, rebuilt by his own proof script ---
buf = io.StringIO()
with redirect_stdout(buf):
    ns = runpy.run_path("/home/hatch/workspace/your_files/core/core_engine_proof.py")
W = ns["W"]; evW = np.linalg.eigvalsh(W)
rW, nW, zfrac = rratio(evW)
sW = np.diff(np.sort(evW)); nzsp = sW[sW > 1e-9]
r_nz = float(np.mean(np.minimum(nzsp[:-1], nzsp[1:]) / np.maximum(nzsp[:-1], nzsp[1:])))
print(f"W (GENESIS pair-adjacency): <r> raw = {rW:.4f}; zero-spacing fraction = {zfrac:.3f}; "
      f"<r> over nonzero spacings = {r_nz:.4f}; distinct eigenvalues = {len(np.unique(np.round(evW,6)))} of 48")

# --- zeta zeros, first 200 ---
mp.mp.dps = 30
ords = [float(mp.im(mp.zetazero(k))) for k in range(1, 201)]
rz, _, _ = rratio(ords)
print(f"zeta zeros 1..200: <r> = {rz:.4f}  (raw ordinates; r-ratio needs no unfolding)")
ords2 = [float(mp.im(mp.zetazero(k))) for k in range(1001, 1201)]
rz2, _, _ = rratio(ords2)
print(f"zeta zeros 1001..1200: <r> = {rz2:.4f}")
print("\nReference constants (Atas et al.): Poisson 0.3863 | GOE 0.5359 | GUE 0.6027")
