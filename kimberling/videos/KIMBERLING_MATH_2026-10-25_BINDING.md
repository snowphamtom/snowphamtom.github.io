# BINDING — KIMBERLING MATH VIDEO (v4)

Each on-screen claim, bound to its evidence. Nothing on screen
without a row below.

- "K[i,j] recursion + 20 terms" → the campaign paper's map;
  walk.c `terms 20` reproduces the published first 20 terms
  exactly (20/20 match).
- "n = 20 backward trace" → the backward trace rule from (20, 20),
  computed step by step in the video's S2a (each step shown).
- "v = 502 trajectory, 1,190 sampled states" → traj_502.txt
  (1,190 real sampled states from the verified reverse walk;
  first (169, 164), last (118850522, 0); d > 0: 586, d < 0: 603,
  d = 0: 1 arrival). The counter reconciles per frame (final:
  sample 1190, row 118,850,522, d = 0).
- "ARRIVED: a(118,850,522) = 502" → walk.c `rev 502`:
  n = 118,850,522, steps = 118,850,353 (= n − 169); gate.c
  verifies the same walk (ADMIT, exact).
- "Row triples proved + injectivity" → Row-Triple Theorem
  (traces ending at row i* ≥ 4 give values in {3i*−4, 3i*−3,
  3i*−2}; triples partition {2,3,4,…}) and the
  Deterministic-Reverse Lemma (at most one preimage → injectivity
  PROVED), both from the campaign paper.
- "Mirror: u_A 62/9 → −31/9; u_B −32 → −16 → −8 → −4; targets
  −12/−10/−8; switch cost (4/3)i + 29/9" → the n = 20 forward
  trace, computed exactly (renorm.c, perspective 5: 0 violations
  over 198,909 steps for n = 1..1000). Switch STATISTICS (means,
  counts over 1,181 walks) are labeled CITED to the campaign
  paper §6, not recomputed in this video.
- "BRIDGE + $300 unclaimed + 29,965/29,991 + 0 stuck +
  surjectivity OPEN" → the merged six-CSV sweep (29,991 targets,
  29,965 hits, 26 capped, 0 stuck in 29,991); the BRIDGE is the
  paper's open statement (every reverse path from (I, 2I−c)
  reaches the diagonal — unproved); the $300 prize is recorded
  in the drop's papers as unclaimed.
- Format figures (1080×1920, 30 fps, 2,880 frames, 96.000 s) →
  ffprobe on the delivered file; SHA-256 in the SPEC.
