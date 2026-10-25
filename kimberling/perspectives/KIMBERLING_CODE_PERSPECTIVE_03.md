# PERSPECTIVE 3 — A CODE (built fully)

The row triples are a codebook. The reverse walk is the decoder.
The decoder has exactly three outcomes — and it is incapable of a
fourth, the false decode.

## The codebook

Row 1: {1}. Row i ≥ 2: {3i−4, 3i−3, 3i−2}. The triples partition the
integers (proved): every integer belongs to exactly one triple, so
every value has exactly one codeword (row) to decode from. No value
is homeless, no value is double-booked.

## Encoder and decoder

- Encoder: n → a(n) by backward trace.
- Decoder: v → n by deterministic reverse walk (v ≥ 8); v < 8 by
  direct table (rows 1–3, "checked directly" — see scope note below).

## Three outcomes, never a fourth

- **DECODED** — the walk reaches (n, n). Receipt: (v, n, steps).
  Certified: a(n) = v by the trace identity.
- **DETECTED_ERROR** — the walk reaches a state with no valid
  preimage. The value is PROVED not a codeword output (at most one
  preimage, and here zero). This is detection, not failure to find.
- **ERASURE** — the budget exhausts. Status unknown, never a guess,
  never a false decode.

**No false decodes, by construction.** The decoder outputs n ONLY on
arrival at (n, n), and arrival certifies a(n) = v. It cannot output a
wrong n the way a probabilistic decoder can. It detects and erases;
it never corrects (never guesses n).

## Verified runs (all recomputed for this build)

- **Roundtrip, 591/591, 0 failures.** Every phase-1 pair: encode(n)
  = v and decode(v) = n.
- **Roundtrip, n = 1..1000: failures 0, detected errors 0,
  erasures 0.** Encode then decode is the identity on the first
  thousand indices.
- **Spot decode:** v = 502 → DECODED, n = 118,850,522,
  steps = 118,850,353.
- **Erasure demo:** v = 3330 at budget 100,000,000 → ERASURE,
  steps = budget exactly. Not an error, not a guess.
- **Detected-error demo (synthetic state, labeled):** (i = 2, d = 2,
  j = 4): even candidate j = −4 invalid, odd candidate j = 3 invalid
  (3 < 3 is false). Zero valid preimages → DETECTED_ERROR.
- **Empirical: 0 detected errors in 29,991 real decodes**
  (29,965 DECODED + 26 ERASURE). The error branch is built, tested,
  and has never fired on a real value.

## Completeness = surjectivity (OPEN)

A complete code decodes every integer. This code decodes every integer
tried except the 26 erasures — and whether every integer decodes at
some budget is exactly the surjectivity question, unproven, $300
unclaimed. So the honest statement is: a code with erasures whose
completeness is open. The erasures are the open question, stated as
erasures, not hidden and not refused.

## Scope catch (found by this build, fixed in this build)

The first roundtrip run showed 4 detected errors: v = 1, 2, 3, 5
(n = 1, 25, 2, 3) — all failing at step 0. Cause: the (I, I−c)
reverse start applies only for v ≥ 8; rows 1–3 do not fit it, and
their start states have no valid preimage. These were FALSE errors
(the values are real: a(1) = 1, a(25) = 2, a(2) = 3, a(3) = 5).
Fix: the decoder now routes v < 8 through the verified direct table
(1→1, 2→25, 3→2, 4→4, 5→3, 6→22, 7→6, each by forward trace), and the
same latent scope bug was fixed in the gate (perspective 1) before it
could mis-verdict a small value. Re-run after the fix: 0 errors.
The code's scope boundary is now in the code, not just in this spec.

## What "fully" means for this perspective

Codebook + encoder + decoder + all three outcomes exercised + both
roundtrips clean + the scope boundary found, fixed, and re-verified
+ completeness stated as open (not claimed, not hidden).
