# PERSPECTIVE 2 — THE ONE-WAY FUNCTION (built fully, premise refuted)

The list claimed: forward cheap, reverse expensive. The build measured it.
The claim is wrong, and this spec records the refutation, not a defense.

## The measurement

Forward cost = backward-trace steps to compute a(n) from n.
Reverse cost = reverse-walk steps to find n from v.

- v = 502: forward 118,850,354 steps, reverse 118,850,353 steps.
- v = 669: forward 653,494,467 steps, reverse 653,494,466 steps.
- Batch, 591 phase-1 pairs, 0 mismatches: total reverse 205,349,937,
  total forward 205,350,528 — difference exactly 591, one per pair.
  Mean reverse 347,461.8, mean forward 347,462.82 — difference exactly 1.
  Max ratio 0.9999999916 (v = 502).

## Why (the identity, not just the numbers)

The forward trace steps i from n down to i*: exactly n − i* steps.
The reverse walk steps i from i*+1 up to n: exactly n − i* − 1 steps.
Difference exactly 1, for every pair, by construction. The batch total
difference (591 = the pair count) is the identity, verified, not a
coincidence.

## The confusion, named

The mirror variables u contract (they halve each forward step) — but
step count does not. Value-contraction was mistaken for cost. The
"cheap forward" intuition came from watching u shrink; the step count
grows with n in both directions. One-way in value, symmetric in cost.

## Conclusions

- **NOT a one-way function by cost.** Forward and reverse cost the
  same (within 1 step). There is no asymmetry to lean on.
- **NOT a proof-of-work.** Verification (forward trace) costs the same
  as finding (reverse walk). A PoW needs cheap verification; this has
  none.
- **NEVER use as a password hash, commitment, or security primitive.**
  Inversion costs the same as evaluation, so an adversary pays no
  premium. This is a mathematical structure, not a security claim.
- **What survives, and it is real:**
  - Zero collisions. Proved (injectivity: at most one preimage, by the
    Deterministic-Reverse Lemma) and checked: a(1..100,000) all
    distinct, 0 collisions.
  - Collision-free addressing. Value ↔ unique n, same cost both ways.
    A canonical bijection-shaped map: injective, and IF surjectivity
    holds, a permutation of the positive integers.
  - The cost meter survives (perspective 11): walk length prices a
    value — but the price is direction-independent.
  - One-way in DIRECTION survives (Taylor: "Math works 1 way"): walks
    never loop back, the reverse path is deterministic, u contracts
    forward. Direction is real; cost asymmetry is not. The phrase is
    about direction, and direction holds.

## Engine and correction note

`~/workspace/kimberling_video/oneway.c` (modes: `pair`, `batch`,
`collide`). The first batch run printed a garbage max-ratio (0x) from
an integer-division bug in the display line; caught, fixed to float,
re-run clean (0.9999999916). The totals, means, and mismatch count
were unaffected.

## What "fully" means for this perspective

The premise was built, measured, and refuted — with the identity that
explains why, the surviving properties separated from the dead ones,
and the security boundary stated plainly. A perspective build that
only confirms its list would be worth less than this one.
