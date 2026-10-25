# PERSPECTIVE 10 — IDENTITY (built fully)

A value's identity is not its numeral. The numeral names it; the
identity LOCATES it and PROVES it:

  identity(v) = (row, position, witness)

- **row:** istar, the row whose triple contains v (partition, PROVED).
- **position:** first / middle / last within the triple (c = 9 / 7 / 5).
- **witness:** the diagonal point n with a(n) = v, IF the reverse
  walk reaches it. For capped values the witness is PENDING — the
  value still has an identity (row, position), but no witness yet.

## The split that matters

Row + position are computable from v alone, instantly, with no walk
(the triple containing v is arithmetic). Only the witness requires
the walk. So most of a value's identity is free; the proof of
admission costs the walk (priced in perspective 11). And identity
does not imply admission: the 26 capped values HAVE identities
(row, position) and NO witness. A system that confuses "has an
identity" with "is admitted" would admit the capped 26 on a
technicality — this one does not.

## Verification (recomputed for this build)

- Engine: `~/workspace/kimberling_video/identity.py` (fourth
  independent implementation of the walk rule).
- **Check 1 — full sweep (six CSVs, merged, conflict aborts):**
  29,991 targets. Every CSV row matched its recomputed row
  (29,991/29,991). Distinct (row, position) pairs: 29,991,
  **0 collisions**. Distinct admitted witnesses n: 29,965,
  **0 collisions** — the empirical shadow of PROVED injectivity
  (perspective 1: every value occurs at most once, so no two
  values can share a witness, in principle, not just in this set).
  Capped identities with witness pending: 26.
- **Check 2 — recomputation (values 1..300, step cap 500,000/lane):**
  admitted 297, **0 mismatches** against CSV entries (row,
  position, witness). In-flight at this cap: v = 147, 173, 242 —
  named, not hidden. (v = 106, in-flight at perspective 9's
  200,000 cap, is admitted here: its walk runs between 200,000
  and 500,000 steps. The in-flight set depends on the cap; the
  identity does not — row and position are known regardless.)
  Values 1..7 use the direct table (rows 1–3, verified by direct
  forward check in perspective 1); the (I, I−c) walk start does not
  fit them, and this script does not pretend otherwise.
- **Check 3 — dedupe demo:** row 168's values [500, 501, 502]
  deduped by row alone collapse to 1 — WRONG, three distinct
  values erased. Deduped by identity they stay 3 — RIGHT. A
  multiset [502, 503, 502, 504, 503, 500, 501, 502] deduped by
  identity gives 5 distinct, exactly the distinct numerals.
  The house law in math form: dedupe by content (identity), never
  by a coarser label (row) or a bare name.

## What "every instance distinct" means here

Twice over: no two values share an identity (29,991 distinct), and
no two admitted values share a witness (29,965 distinct). The
first is the partition (proved); the second is injectivity
(proved). The checks above confirm both on the full sweep — they
do not establish them; the proofs do. The checks catch a corrupted
record, not a false theorem.

## The boundary (what "identity" does NOT mean)

- NOT the numeral: two entries with the same numeral are the same
  value (dedupe to one), but the numeral alone does not locate it
  (row, position) or prove it (witness). A bare list of numerals
  is a list of names, not identities.
- NOT existence: a capped value's identity is real and its witness
  is pending. "Has an identity" and "is admitted" are different
  claims, and only the witness bridges them.
- NOT a claim about surjectivity: identity covers every value that
  EXISTS in the sweep (29,991 named targets). Whether every
  positive integer has a witness — i.e., whether the identity
  system covers all of ℕ — is the open BRIDGE, not settled here.

## What "fully" means for this perspective

The identity defined (row, position, witness) + the free/expensive
split stated + uniqueness checked on the full sweep (29,991
identities, 29,965 witnesses, 0 collisions each) + recomputation
matched (297 admitted, 0 mismatches, in-flight named) + the dedupe
law demonstrated (row-collapse wrong, identity-collapse right) +
the boundary stated. Statistics claimed only where measured;
uniqueness claimed only where proved or checked.
