# PERSPECTIVE 6 — BISECTION (built fully, efficiency corrected)

Each step halves a mirror variable, like bisection halving an interval.
The walk length is the search cost. The distribution is a long tail.
And the efficiency is NOT bisection's — that part of the analogy is
wrong, and this spec says so.

## The mechanism (halving, real)

Forward: each step halves u (u_A flips and halves on even steps, u_B
halves on odd steps — perspective 5). Reverse: each step doubles u.
The walk narrows (forward) or widens (reverse) by a factor of 2 per
level, exactly like bisection narrowing an interval by half per
comparison. The mechanism is real.

## The search cost (measured distribution)

Walk length = steps to find n from v = n − i* − 1 (structural: i
climbs one row per step from the target row to the answer row).
Recomputed over the full sweep (29,965 admitted walks, same six-CSV
merge, 0 conflicts):

- Walks: 29,965. Total steps: 148,075,290,444.
- Mean: 4,941,608.2. Median: 12,049. p90: 424,351. p99: 36,304,994.
- Max: 4,733,476,427 (v = 24086, n = 4,733,484,458).
- 21,571 walks ≤ 50,000 steps; 1,946 walks > 1,000,000 steps;
  172 walks > 100,000,000 steps.
- Five longest: v = 15146 (4,076,008,343 steps), v = 27977
  (4,199,138,249), v = 7113 (4,404,760,543), v = 21717
  (4,641,639,054), v = 24086 (4,733,476,427).
- 21,059 walks have n ≤ 50,000 (the small-answer bulk).

Mean ≫ median by a factor of ~410: usually short, with a very long
tail. The tail is the story: a handful of values cost billions of
steps while the typical value costs twelve thousand.

## Switches pile up ON long walks (not the other way around)

Phase-1 walks (591), reverse walk with branch (even/odd preimage)
counted per step:

- Mean steps: 347,461.8. Mean switches: 173,752.6 (about one switch
  every 2 steps — branches alternate near-randomly, consistent with
  the cited geometric run-length ratio ≈ 1/2).
- Max steps and max switches are the SAME walk: v = 502
  (118,850,353 steps, 59,431,053 switches).

Switches do not lengthen walks: steps are fixed by the answer
(n − i* − 1) regardless of branch. Long walks accumulate switches
because they have more steps to switch in. The listed phrasing
("long tail when switches pile up") reverses the causation; the
corrected statement is: switches pile up when walks run long, at
about one switch per two steps.

## The efficiency correction

Bisection on a sorted array costs O(log N). This walk costs O(n) —
linear in the answer, not logarithmic in the problem size. The
halving is in the mirror VARIABLE (u), not in the search SPACE (i
climbs linearly, one row per step). So the perspective keeps
bisection's mechanism (halving per level) and loses bisection's
efficiency (log cost). A walk that halves u at every step but still
takes 4.7 billion steps is not an efficient search — it is a
halving walk with a linear bill. The bill is the content of
perspective 11 (certification cost); this perspective is its shape.

## Engine

`~/workspace/kimberling_video/bisect_stats.py` (full-sweep
distribution) and `~/workspace/kimberling_video/bisect.c` (phase-1
switch counts; step counts re-verified against the CSV, 0
mismatches).

## What "fully" means for this perspective

The mechanism (halving) + the measured cost distribution (mean,
median, percentiles, tail, five longest) + the switch causation
corrected (switches follow length, not the reverse) + the efficiency
correction (linear, not log). The analogy was kept where it holds
and cut where it doesn't.
