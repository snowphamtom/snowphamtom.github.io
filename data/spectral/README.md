# Spectral Measurements — the GENESIS Operator, the Phase Twist, and the Zeta Controls

Taylor Heller / Monsters Ink LLC — published 2026-10-22.

Which universality class do the spectra in this corpus actually sit in?
Measured with the r-ratio statistic ⟨r⟩ (Atas et al. 2013), which needs no
unfolding. Reference constants: Poisson 0.3863 · GOE 0.5359 · GUE 0.6027.
The base matrix is W, the GENESIS pair-adjacency operator — its full data
is published in the GENESIS Census drop (`../genesis-census/`).

## Controls (seeded random-matrix ensembles, n = 48, 300 trials)

- GOE: ⟨r⟩ = 0.5332 ± 0.0461
- GUE: ⟨r⟩ = 0.5993 ± 0.0424
- Poisson: ⟨r⟩ = 0.3892 ± 0.0494

The controls land on their classes; the instrument is calibrated.

## The corpus operators

- **H14 syndrome matrix:** rank 7 of 48 — 41-fold degenerate zero
  eigenvalue. Spacing statistics are *undefined* on it; no ⟨r⟩ is quoted.
- **W (pair-adjacency):** Σλ² = 191,808 (build check exact); 27 distinct
  eigenvalues of 48; ⟨r⟩ = 0.1688 (real solver) — far below Poisson.
  21 of 47 spacings are < 1e-6, so W's own ⟨r⟩ is a cluster-noise band,
  not a class measurement: the spectrum is symmetry-clustered.
- **Zeta zeros (the target class):** ⟨r⟩ = 0.6150 (zeros 1–200),
  0.6183 (zeros 1001–1200) — GUE, as Montgomery–Odlyzko established.

## The phase twist — can the corpus's own angle reach GUE?

W's magnitudes, phases imposed (`phase_twist_results.md`; fresh run in
`results_phase_twist.txt` reproduces it exactly):

- Uniform twist at the lynchpin angle 15.130102°: ⟨r⟩ = 0.2683,
  degeneracy fully lifted (48/48 distinct) — still below Poisson.
- Uniform twist at the canon angle 53.130102°: ⟨r⟩ = 0.3139.
- Per-door twist φ_ab = W_ab · 53.130102°: ⟨r⟩ = 0.3224.
- Full θ scan 0–90°: plateau 0.208–0.344, max at 22.5°. **The canon
  angle is mid-pack, not a peak.**
- Random phases on the same magnitudes: ⟨r⟩ = 0.6012 ± 0.0394 — **GUE**.
- Random signs (real symmetric): ⟨r⟩ = 0.5299 ± 0.0440 — GOE.

Reading: a single global angle never reaches GUE at any θ. What reaches
GUE is phase *disorder* — an independent phase per pair. That is generic
universality, not a corpus signature: GUE in by hand, GUE out.

## Riemann spot-check (computed, not proof)

`riemann_check.py` at 50-digit precision: the first 25 zeta zeros lie on
the critical line with max |ζ| residual 1.75e-49; off-line probes at the
same heights do not vanish; N(100) counts 29 zeros against a
Riemann–von Mangoldt main term of 29.0023. Numerical verification of
known results — evidence the tooling is sound, nothing more.

## Scope — read this before citing

This drop measures **spectral class only**. It does not construct, and
does not claim, a Hilbert–Pólya operator: no self-adjoint operator with
zeta-regularized det(s − H) = ξ(s) exists in this corpus, and a full
excavation of the corpus's candidates (2026-10-22) found none. Even a
perfect ⟨r⟩ would be necessary-flavored evidence, never the determinant
identity. The negative result is published because it is the measured
one.

## Files

- `spectral_class.py` — controls, H14, W, zeta zeros
- `phase_twist.py` — the twist experiment · `phase_twist_results.md` —
  its recorded results · `results_phase_twist.txt` — fresh run, 2026-10-22
- `riemann_check.py` · `results_riemann_check.txt` — fresh run, 2026-10-22
- `SHA256SUMS.txt` — checksums for every file in this folder
