# PERSPECTIVE 4 — A HALTING QUESTION (built fully, premise corrected)

The reverse walk as a program. State (i, d). Step: i → i + 1.
The program has three fates — and the listed premise got one of them
wrong, so this spec corrects it first.

## The correction

The list claimed: "the only failure mode is non-termination (never
stuck, never loops back; both proved)." Half of that is wrong.

- **Never loops: PROVED.** Each reverse step sets i → i + 1 exactly
  (asserted on every step by the halting program below). i is strictly
  monotone, so no state (i, d) can repeat. "Doesn't halt" therefore
  means infinite ascent, never a cycle. This half is real, and it is
  what makes this halting question unusually clean.
- **Never stuck: NOT proved — observed.** The campaign paper says
  "No target in 11,991 has ever produced a stuck path" (empirical),
  and the decision procedure itself USES stuck as a certificate ("a
  stuck path certifies v never appears"). If never-stuck were proved,
  that certificate branch could not exist. Stuck is a live branch,
  empirically absent (0 in 29,991), not proved absent.

## The three fates

- **HALTS** — reaches d = 0 (the diagonal). Receipt: (v, n, steps).
  Certified: a(n) = v.
- **STUCK** — reaches a state with no valid preimage. A crash that is
  a PROOF: it certifies v never appears. Not an error state — a
  certificate state. (This is perspective 1's REFUSE, seen from the
  program's side.)
- **RUNS ON** — neither halts nor sticks: ascends forever. Walking can
  never certify this fate; only a proof of non-termination could.

Surjectivity = does every target-started walk halt? The census below
is the current state of that question, not its answer.

## The halting program

`~/workspace/kimberling_video/halt.c` (mode: `halt V [BUDGET]`).
It asserts the no-loop invariant (inew == i + 1) on every step, so
the executed walk carries its own loop-freedom proof. Outcomes:
HALTS / STUCK / UNKNOWN (budget exhausted — still ascending, fate
undecided; UNKNOWN is not RUNS ON, it is "not yet decided").

## Verified runs (all recomputed for this build)

- **Census (recomputed from the six sweep CSVs, same merge as the
  frontier video, conflict aborts — 0 conflicts): targets 29,991,
  HALTS 29,965, UNKNOWN 26, rows 4..10,000, zero rows with ≠3 targets.**
- **Spot halt:** v = 502 → HALTS, n = 118,850,522,
  steps = 118,850,353 (verified through the gate, the one-way, and
  the code builds, and by the halting program's own assert-run on the
  full walk: the no-loop invariant asserted on all 118,850,353 steps,
  zero failures).
- **Spot unknown:** v = 3330 at budget 100,000,000 → UNKNOWN,
  steps = budget exactly. Still ascending; fate undecided. It has
  three possible fates: halt later, stick later (→ certified REFUSE),
  or run forever. The budget tells us none of the three.
- **Stuck, empirical: 0 in 29,991.** The STUCK branch is built and
  tested on synthetic states (perspectives 1 and 3); it has never
  fired on a target-started walk.

## What the halting framing buys

- It separates the three fates cleanly: halt (certified yes), stuck
  (certified no), runs-on (uncertifiable by walking). Most halting
  talk blurs these; this walk forces them apart.
- It explains perspective 1: the gate's REFUSE branch is provably
  unreachable only if never-stuck were proved — it is not, so REFUSE
  stays a live branch with zero firings, not a dead branch.
- It states the open question exactly: surjectivity is the claim
  that the RUNS ON and STUCK fates never occur for target-started
  walks. The 26 unknowns are the only candidates for either fate.

## What "fully" means for this perspective

The program + the loop-freedom proof (executed as asserts) + the
recomputed census + the corrected premise (never-loops proved,
never-stuck observed) + the three fates with their certificate
statuses distinguished. The premise was not defended; it was fixed.
