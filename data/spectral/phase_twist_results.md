# Phase-Twist Test — Results (2026-10-22, ordered by Taylor)

Script: `~/workspace/millennium/phase_twist.py`. Statistic: r-ratio ⟨r⟩ (Atas et al. 2013).
Reference: Poisson 0.3863 | GOE 0.5359 | GUE 0.6027 | zeta zeros measured (PKT-014): 0.6150 / 0.6183.
Base matrix: W from `core_engine_proof.py` (doors per pair). Build check exact: Σλ² = 191,808; 27 distinct eigenvalues of 48; ⟨r⟩ = 0.1688 (real solver).

## Measured

| Construction | ⟨r⟩ | Distinct eigs | Note |
|---|---|---|---|
| W untwisted | 0.1688 / 0.2081 | 27/48 | real vs complex solver — same spectrum (max Δλ = 2.27e-13); 21 of 47 spacings < 1e-6, so W's own ⟨r⟩ is a cluster-noise band. Far below Poisson either way. |
| Uniform twist θ = 15.130102° (lynchpin) | 0.2683 | 48/48 | degeneracy fully lifted |
| Uniform twist θ = 53.130102° (canon) | 0.3139 | 48/48 | still below Poisson 0.3863 |
| Per-door twist φ_ab = W_ab · 53.130102° | 0.3224 | 48/48 | corpus-determined phases; same clustered regime |
| θ scan 0–90° (2.5° steps) | 0.208–0.344 | — | plateau; max at 22.5° (0.3436); **canon angle is mid-pack, no peak** |
| Random phases, same magnitudes (300 trials, seed 20261022) | **0.6012 ± 0.0394** | — | GUE class |
| Random-phase seed check (200 trials × seeds 7 / 12345 / 999) | 0.6002 / 0.6032 / 0.6016 | — | seed-robust |
| Random signs, real symmetric (300 trials) | 0.5299 ± 0.0440 | — | GOE class |

## Reading

1. The phase does the first required job: any nonzero twist breaks time-reversal symmetry and lifts all 21 degenerate spacings — 48/48 distinct eigenvalues.
2. A **single global angle does not reach GUE** — not at the canon angle, not at the lynchpin, not anywhere in 0–90°. A uniform twist puts the same flux through every triangle; the spectrum keeps the corpus's clustering (sub-Poisson). The canon angle is not distinguished by the data.
3. What reaches GUE is **phase disorder** — an independent phase per pair, on W's own magnitudes. That is generic universality, not a corpus signature: the magnitudes were never the obstacle, and random phases landing on 0.6027 is the Berry–Keating trap in miniature (GUE goes in by hand, GUE comes out).
4. Scope: this tests spectral class only. Even a perfect ⟨r⟩ would be necessary-flavored evidence; the determinant identity det(s − H) = ξ remains untouched and absent.
