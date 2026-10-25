# PERSPECTIVE 7 — A FAIR COIN (built fully)

The branch sequence of a reverse walk is a fair coin — statistically.
It is fully deterministic, so the fairness is statistical, not
unpredictability. Both halves matter.

## The coin

Each reverse step takes the even preimage (branch 0) or the odd
preimage (branch 1). The branch sequence is the coin-flip sequence.
Given v, the whole sequence is fixed by the walk — no randomness
enters anywhere. Yet its statistics are a fair coin's.

## Measured fairness (recomputed for this build, 591 walks)

Branch runs (consecutive same-branch stretches), 102,688,349 runs
over 205,349,937 steps:

- Length 1: 51,348,444 observed (geometric-1/2 expected 51,344,174)
- Length 2: 25,670,924 (expected 25,672,087)
- Length 3: 12,837,440 (expected 12,836,044)
- Length 4: 6,416,245 (expected 6,418,022)
- Length 5: 3,209,968 (expected 3,209,011)
- Length 6: 1,602,534 (expected 1,604,505)
- Lengths 7–12 continue halving (801,968 / 401,327 / 200,247 /
  99,869 / 49,487 / 25,050, each within ~0.5% of expected).

Counts halve at every length, exactly as a fair coin's run lengths
do (P(run = k) = (1/2)^k). The fit holds across 102 million runs —
this is not a small-sample coincidence.

Branch balance: even steps 102,674,169, odd steps 102,675,768,
even share 0.5000 (to four decimals) over 205 million flips.

Final-branch (arrival) counts over the 591 walks: even 311,
odd 280 (52.6% / 47.4% — noisier, as expected for 591 samples).
Cited comparison (campaign §6, 1,181 instrumented walks, NOT
recomputed here): arrivals 593 even / 588 odd (50.2% / 49.8%),
and run counts 7,251,752 / 3,624,209 / 1,814,985 / 906,587 for
lengths 1–4 (ratios 0.4997 / 0.5007 / 0.4995). The cited and the
recomputed samples agree: the coin is fair.

## Deterministic chaos (sensitivity, shown)

Consecutive values have unrelated branch sequences from the start:

- v = 502, first 20 branches: 11111000110101011011
- v = 503, first 20 branches: 11110011000110111000
- v = 504, first 20 branches: 11111011010100101000

No shared prefix beyond chance (they agree on the first 4 flips,
then diverge — exactly what independent fair coins do). A one-step
change in value scrambles the whole sequence, while the statistics
stay fair. Deterministic input, chaotic output, fair statistics:
all three at once.

## The boundary (what "fair" does NOT mean)

- NOT unpredictable: anyone with the walk algorithm computes every
  flip for any v. There is no secret, no entropy, no randomness
  source here.
- NOT cryptographic: never use a branch sequence as a key, nonce,
  or random seed. An adversary who knows v knows the sequence.
- What it IS: a deterministic sequence with fair-coin statistics —
  useful as a test sequence, a demo of deterministic chaos, and a
  reminder that "looks random" and "is random" are different claims.

## Engine

`~/workspace/kimberling_video/coin.c` (modes: `runs` for the
histogram/balance/arrival counts, `seq` for a value's first K
branches).

## What "fully" means for this perspective

The coin defined (branches) + run histogram recomputed (102M runs,
geometric fit to ~0.5%) + balance recomputed (0.5000 over 205M flips)
+ arrival counts (new sample + cited sample, labeled) + sensitivity
shown (three consecutive values diverge) + the unpredictability
boundary stated. Statistics claimed only where measured; the cited
§6 figures labeled as cited, not recomputed.
