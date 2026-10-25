# PERSPECTIVE 11 — CERTIFICATION COST (built fully)

A value's certification cost is the number of steps its reverse walk
takes to reach the diagonal — metered in steps ACTUALLY WALKED
(counted by the engine, never estimated, never modeled). The gate
(perspective 1) certifies ADMIT by walking; the walk length IS the
price of the certificate.

## The price list (all recomputed for this build)

- **Direct (v < 8): 0 walk steps.** Answered from the direct table,
  not by walking.
- **Zero-step certificates: exactly 3 values — 10, 15, 20.** Their
  target start IS on the diagonal (d = 0 at step 0: I = c — row 4
  last, row 6 middle, row 8 first). The cheapest possible
  certificate is free, and only three values hold one.
- **Ordinary certificates: steps = n − istar − 1** (perspective 2:
  reverse cost = forward cost − 1, exactly). Named prices:
  v = 502 → 118,850,353 steps (n = 118,850,522);
  v = 669 → 653,494,466 steps (n = 653,494,691);
  v = 24086 → 4,733,476,427 steps (n = 4,733,484,458) — the most
  expensive certificate in the sweep.
- **UNKNOWN: the whole budget, spent, with no certificate.** The
  certifier chooses the budget; the UNKNOWN price is whatever
  budget was spent. v = 3330 cost 5,000,000,000 steps at the full
  budget (live gate re-walk, perspective 1) and certified nothing.
- **REFUSE: 0 steps, synthetic only.** State (2, 2, 4) stuck at
  step 0. No real value has ever stuck (0 in 29,991), so no real
  REFUSE price is measured.

## The distribution (recomputed, all totals reconcile)

- Admitted: 29,965 certificates for 148,075,290,444 steps.
  Min 0, median 12,049, mean 4,941,608.2, p90 424,351,
  p99 36,304,994, max 4,733,476,427. Mean ≈ 410× median — the long
  tail from perspective 6, now priced: most certificates are cheap
  (half cost ≤ 12,049 steps) and a few are enormously expensive.
- Phase-1 subset (rows 4..200): 591 certificates for 205,349,937
  steps, mean 347,461.8, median 247. The early rows are far cheaper
  than the full sweep — price grows with row, as steps ≈ n does.
- Uncertified spend: 130,000,000,000 steps (26 capped ×
  5,000,000,000) — **46.7% of all steps ever spent produced zero
  certificates.** Nearly half the compute bought nothing, because
  the capped walks are the longest ones. That is the cost of
  certifying at the frontier: the budget is spent whether or not
  the certificate issues.

## Verification (recomputed for this build)

- Engine: `~/workspace/kimberling_video/cost.py` (merge of the six
  CSVs, conflict aborts; every total reconciled against the
  perspective-6 figures — a mismatch fails the run).
- **COST VERDICT: all totals reconcile** — targets 29,991,
  admitted 29,965, capped 26; certified 148,075,290,444;
  uncertified 130,000,000,000; grand 278,075,290,444. Every price
  is a counted step total, not an estimate.
- Named prices cross-checked against the C engines (walk.c rev
  502 / rev 669, gate.c's 591/591 exact re-walk, the live 5e9
  re-walk of 3330) — all match the CSV figures used here.

## The boundary (what "cost" does NOT mean)

- NOT time: steps are the meter, not seconds. The 5e9-step re-walk
  of 3330 took 139,877 ms under contention vs ~56 s unloaded —
  same price, different wall time. Time depends on hardware and
  load; steps do not.
- NOT worth: a long walk is not "more true" than a short one. The
  certificate is binary (ADMIT or not); price ≠ worth. This is the
  value law in cost form: value = new data × field consequence,
  not steps spent. The most expensive certificate (v = 24086,
  4.7B steps) is worth exactly one admission, same as the free
  ones (10, 15, 20).
- NOT the price of the proofs: the lemmas (injectivity, triples,
  no-loops) were proved once and cost 0 per certificate
  thereafter. The marginal cost of a certificate is the walk; the
  fixed cost is the proof. Conflating them would price every
  certificate as if the theorems had to be re-proved.
- NOT a prediction: the price of an uncertified value's
  certificate (if it ever issues) is unknown — it is at least the
  budget already spent, plus whatever further walking it takes.
  The 26 capped have each already cost 5,000,000,000 steps with no
  certificate to show for it, and no price can be quoted for their
  completion.

## What "fully" means for this perspective

The cost defined (steps actually walked) + the price list (direct,
zero-step, ordinary, UNKNOWN, REFUSE) + the distribution
recomputed (median, mean, p90, p99, max) + the uncertified-spend
share (46.7%, 0 certificates) + all totals reconciled + the
boundary stated (not time, not worth, not the proofs' price, not
a prediction). Statistics claimed only where counted; prices
quoted only where walked or budgeted.
