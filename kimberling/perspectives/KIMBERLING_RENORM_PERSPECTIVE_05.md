# PERSPECTIVE 5 — RENORMALIZATION (built fully)

Forward steps contract the mirror variables by exactly 1/2, and the
targets sit at fixed values on every row. That is scale invariance
with fixed points — exact, not asymptotic.

## The contraction (exact identities, not approximations)

In the forward trace (i, d), s = d + i:

- Even step (s even): u_A = d + i/3 + 2/9, and u_A' = −u_A/2.
  Contract AND flip. Carried exactly as a numerator over 9.
- Odd step (s odd): u_B = d − i − 3, and u_B' = u_B/2. Contract.

These are algebraic identities (derived in the campaign's mirror
framework), and this build verifies them on real traces rather than
citing them: n = 20 step by step (u_A 62/9 → −31/9, the contract-and-
flip, visible; u_B −32 → −16 → −8 → −4, halving each odd step), and
a batch of n = 1..1000 (198,909 steps, 0 violations).

## The fixed points (targets at fixed u_B, every row)

A reverse-walk start (target) is (I, I−c), c ∈ {9, 7, 5}. Its u_B:
u_B = (I−c) − I − 3 = −c − 3. The row I cancels exactly.

- Triple first value (c = 9): u_B = −12, on every row.
- Triple middle value (c = 7): u_B = −10, on every row.
- Triple last value (c = 5): u_B = −8, on every row.

Verified census over the 591 phase-1 targets: u_B = −12: 197,
u_B = −10: 197, u_B = −8: 197, other: 0. Exact thirds. The target
condition does not mention the row — that is scale invariance: the
same three fixed values label the three positions within each triple,
at row 4 and at row 10,000 alike.

## The switch cost (the coupling term)

The two centerings evolve independently (branch-autonomy) except at
branch switches, where they couple by exactly:

u_A − u_B = (4/3)i + 29/9

Verified: 98,712 switches across the 1..1000 batch, 0 violations
(the check uses the switch state's own i; that interpretation is the
one the data confirms). This single term is what a surjectivity proof
must control — it is the only place the two mirror tracks touch.

## The renormalization reading (and its limits)

- Forward = coarse-graining: each step halves the mirror variable
  (the RG flow toward small u). Reverse = refining: each step doubles
  it (flowing away from the fixed values toward the diagonal).
- The fixed points are the three target u_B values: under the
  row-to-row rescaling, the target condition is invariant.
- Limits, stated plainly: this is an ANALOGY, and in one way it is
  stronger than textbook RG — the scaling here is discrete (×2 per
  step) and EXACT, not an asymptotic fixed point approached in a
  continuum limit. There is no continuum limit, no critical exponent,
  no field theory claimed. What is real is the exact self-similarity:
  the same contraction, the same three fixed values, at every scale.

## Engine

`~/workspace/kimberling_video/renorm.c` (modes: `trace`, `batch`,
`targets`). u_A carried as an exact integer numerator over 9 — no
floating point anywhere in the checks.

## What "fully" means for this perspective

Contraction identities verified step by step + batch (198,909 steps,
0 violations) + switch-cost identity verified (98,712 switches,
0 violations) + fixed-point census exact (197/197/197) + the analogy
with its limits stated, not oversold.
