# PERSPECTIVE 1 — THE GATE (built fully)

The Kimberling decision procedure, built as a working gate. Every value
gets exactly one verdict, and every verdict carries a receipt.

## The mapping (property → gate behavior)

- Row-triple partition (proved): each value belongs to exactly one row,
  so the gate always knows where to start. No value is ever homeless.
- Deterministic reverse (proved, at most one preimage): the path from a
  value is unique. The gate never searches, never branches, never guesses.
- Never stuck (proved three ways) + never loops back (proved): the only
  way a real path fails is by running past the budget. That is why the
  third verdict exists and why it is not a refusal.
- One-way (Taylor: "Math works 1 way"): forward contracts, reverse
  expands. The gate walks the expensive direction on purpose — that is
  what certification costs.

## Verdicts (exact)

- **ADMIT** — the reverse path reaches the diagonal (n, n). Receipt:
  (v, n, steps). Certified: a(n) = v by forward trace.
- **REFUSE** — the reverse path reaches a state with no valid preimage.
  Receipt: the stuck state + both invalid candidates. This is a proof
  the value never appears (Deterministic-Reverse Lemma: at most one
  preimage, and here zero).
- **UNKNOWN** — the path is still running when the step budget exhausts.
  Receipt: (v, steps = budget). This is a verdict about the budget,
  never about the value. **UNKNOWN is never REFUSE.** A gate that
  refused on budget exhaustion would be lying.

## Engine

`~/workspace/kimberling_video/gate.c` (C, stdlib only). Modes: `verdict`,
`verify`, `stuckscan`, `findsmall`. The reverse walk is the same (i, d)
walk verified against the campaign tables (see below), not a new
invention: the gate is the decision procedure, with verdicts and
receipts wrapped around it.

## Verified runs (all recomputed for this build)

- **Batch ADMIT: 591/591, 0 mismatches.** Every phase-1 target
  (i* = 4..200) admitted with the exact (n, steps) from the campaign
  CSV. Total steps 205,349,937 (matches the campaign total).
- **Spot ADMITs:** v = 502 → n = 118,850,522, steps = 118,850,353.
  v = 669 → n = 653,494,691, steps = 653,494,466. Both match the record.
- **Small values 1–7, all ADMIT:** v=1 → n=1; v=2 → n=25; v=3 → n=2;
  v=4 → n=4; v=5 → n=3; v=6 → n=22; v=7 → n=6. Each confirmed by
  forward trace (a(n) = v recomputed).
- **UNKNOWN, budget demo:** v = 3330 at budget 100,000,000 →
  {"verdict":"UNKNOWN","steps":100000000}. Steps equal the budget
  exactly: the walk was cut off by the budget, not by the math.
- **UNKNOWN, live confirmation at full cap (2026-10-25):** v = 3330
  re-walked by the gate itself to the full 5,000,000,000-step budget →
  {"verdict":"UNKNOWN","n":-1,"steps":5000000000}. The sweep-record
  UNKNOWN is now a live-computed UNKNOWN for this value.
- **UNKNOWN, the 26 sweep-capped (5,000,000,000-step budget, sweep
  record — the same procedure at the same budget):** (row, v):
  (1111, 3330), (1270, 3807), (1971, 5910), (2287, 6859),
  (3253, 9756), (4114, 12339), (4395, 13182), (4432, 13294),
  (5366, 16094), (5424, 16268), (6247, 18738), (6619, 19853),
  (6718, 20152), (6834, 20499), (6885, 20652), (7688, 23060),
  (8271, 24810), (8295, 24882), (8321, 24959), (8649, 25945),
  (9077, 27227), (9450, 28346), (9501, 28501), (9681, 29040),
  (9796, 29384), (9898, 29691). Each: hit = 2, n = −1,
  steps = 5,000,000,000 in the merged sweep.
- **REFUSE, branch demonstrated (synthetic state, labeled):**
  state (i=2, d=2, j=4): even candidate j=−4 invalid (< 1), odd
  candidate j=3 invalid (3 < 2·3−3 = 3 is false). Zero valid
  preimages → REFUSE. The scan also returns degenerate states
  (d = 0, j < 1) which the gate never evaluates: it stops at d = 0,
  and columns start at 1.
- **REFUSE, empirical fact: 0 in 29,991 real targets.**
  29,965 ADMIT + 26 UNKNOWN + 0 REFUSE. The refuse branch is built,
  tested, and has never fired on a real target.

## What the gate does NOT claim

- It does not prove surjectivity. ADMIT counts are evidence, not proof.
- It does not refuse the 26. They are UNKNOWN at every budget tried.
- It does not claim the REFUSE branch has fired on a real value. It
  has not. The branch is demonstrated on synthetic states so that if
  it ever fires, the receipt format is already proven.
- Small values (v < 8) are admitted by direct forward check, not by
  the reverse procedure (which is stated for v ≥ 8). Both routes are
  labeled in the receipts' provenance, not mixed.

## What "fully" means for this perspective

Engine + all three verdict branches exercised + every count reconciled
against the campaign record (591/591, 29,965/29,991, 26 named) + this
spec. Nothing sampled, nothing transcribed: the batch, the spots, the
small values, the budget demo, and the stuck-state demo were all
recomputed by the gate itself for this build.
