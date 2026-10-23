#!/usr/bin/env python3
"""PHASE-TWIST TEST (ordered by Taylor, 2026-10-22 ~18:59 CT).
Question: PKT-014 found the corpus pair-adjacency W is real-symmetric and
symmetry-clustered (<r> = 0.1688, 27 distinct eigenvalues of 48) - it cannot
sit in the GUE class the zeta zeros occupy (0.6027, Atas et al.).
Does weighting the interactions with the corpus's own phase - the 3-4-5
rotation angle 53.130102 deg (= arctan(4/3), the angle of (3+4i)/5) and the
lynchpin 15.130102 deg - move the spectrum into the GUE class?

Constructions (fixed before measuring; no fitting):
  A. Uniform twist:  H_ab = W_ab * e^{+i*theta} (a<b), conj (a>b), diag real.
  B. Per-door twist:  phi_ab = W_ab * 53.130102 deg (phase accumulates with
     interaction strength; fully determined by corpus data).
Controls: theta = 0 must reproduce W exactly; random-phase ensemble (same
magnitudes, iid uniform phases, 300 seeded trials) tests whether ANY phases
do this; random-sign real ensemble tests the real-symmetric side.
Statistic: r-ratio <r> (Atas et al. 2013), unfolding-free.
Reference: Poisson 0.3863 | GOE 0.5359 | GUE 0.6027.
Single-matrix yardstick: PKT-014's GUE control at n=48 gave sd 0.0424."""
import io, runpy
import numpy as np
from contextlib import redirect_stdout

def rratio(eigs):
    e = np.sort(np.asarray(eigs, dtype=float))
    s = np.diff(e)
    r = np.minimum(s[:-1], s[1:]) / np.maximum(s[:-1], s[1:])
    return float(np.mean(r)), float(np.std(r)), len(np.unique(np.round(e, 6))), float(np.mean(s == 0))

buf = io.StringIO()
with redirect_stdout(buf):
    ns = runpy.run_path("/home/hatch/workspace/your_files/core/core_engine_proof.py")
W = np.asarray(ns["W"], dtype=float)
evW = np.linalg.eigvalsh(W)
rW, _, distW, _ = rratio(evW)
print(f"BUILD CHECK  W: sum lambda^2 = {np.sum(evW**2):.1f} (canon 191808); "
      f"distinct eigenvalues = {distW} of 48 (PKT-014: 27); <r> = {rW:.4f} (PKT-014: 0.1688)")
assert abs(np.sum(evW**2) - 191808) < 1 and distW == 27 and abs(rW - 0.1688) < 0.001
print(f"W diagonal: min {W.diagonal().min():.0f}, max {W.diagonal().max():.0f}; "
      f"off-diag range {W[~np.eye(48, dtype=bool)].min():.0f}..{W.max():.0f}\n")

CANON = 53.13010235415598   # arctan(4/3), the 3-4-5 rotation
LYNCH = 15.13010235415598   # canon - 38 deg

def twist(theta_deg, per_door=False):
    if per_door:
        ph = np.deg2rad(CANON) * W
    else:
        ph = np.full_like(W, np.deg2rad(theta_deg))
    H = np.zeros((48, 48), dtype=complex)
    iu = np.triu_indices(48, 1)
    H[iu] = W[iu] * np.exp(1j * ph[iu])
    H = H + H.conj().T
    np.fill_diagonal(H, W.diagonal())
    return np.linalg.eigvalsh(H)

print("=== Construction A: uniform twist ===")
for name, th in (("theta = 0 (control)", 0.0), ("LYNCHPIN 15.130102 deg", LYNCH), ("CANON 53.130102 deg", CANON)):
    r, sd, dist, zf = rratio(twist(th))
    print(f"  {name:>24}: <r> = {r:.4f} (sd of ratios {sd:.4f}); distinct eigs = {dist}/48; zero-spacing frac = {zf:.3f}")

print("\n=== Construction B: per-door twist (phi_ab = W_ab * 53.130102 deg) ===")
r, sd, dist, zf = rratio(twist(0.0, per_door=True))
print(f"  {'per-door canon':>24}: <r> = {r:.4f} (sd of ratios {sd:.4f}); distinct eigs = {dist}/48; zero-spacing frac = {zf:.3f}")

print("\n=== Theta scan, construction A (deg : <r>) ===")
scan = []
for th in np.arange(0.0, 90.01, 2.5):
    r, _, _, _ = rratio(twist(float(th)))
    scan.append((float(th), r))
line = "  ".join(f"{th:.0f}:{r:.3f}" for th, r in scan)
print(" ", line)
best_th, best_r = max(scan, key=lambda t: t[1])
print(f"  scan max: theta = {best_th:.1f} deg, <r> = {best_r:.4f}")

rng = np.random.default_rng(20261022)
iu = np.triu_indices(48, 1)
print("\n=== Ensembles (same magnitudes |W|, 300 trials, seed 20261022) ===")
rs = []
for _ in range(300):
    ph = rng.uniform(0, 2 * np.pi, size=len(iu[0]))
    H = np.zeros((48, 48), dtype=complex)
    H[iu] = W[iu] * np.exp(1j * ph)
    H = H + H.conj().T
    np.fill_diagonal(H, W.diagonal())
    rs.append(rratio(np.linalg.eigvalsh(H))[0])
print(f"  random phases (complex Hermitian): <r> = {np.mean(rs):.4f} +- {np.std(rs):.4f}")
rs = []
for _ in range(300):
    sg = rng.choice([-1.0, 1.0], size=len(iu[0]))
    H = np.zeros((48, 48))
    H[iu] = W[iu] * sg
    H = H + H.T
    np.fill_diagonal(H, W.diagonal())
    rs.append(rratio(np.linalg.eigvalsh(H))[0])
print(f"  random signs (real symmetric):      <r> = {np.mean(rs):.4f} +- {np.std(rs):.4f}")
print("\nReference: Poisson 0.3863 | GOE 0.5359 | GUE 0.6027 | zeta zeros measured 0.6150 / 0.6183 (PKT-014)")
