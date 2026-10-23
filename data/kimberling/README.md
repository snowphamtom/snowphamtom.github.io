# The Kimberling Shuffle — Injectivity Proof and the Located Values

Taylor Heller / Monsters Ink LLC — published 2026-10-22.

Kimberling's Problem 2 (on the sequence OEIS A007063) asks: *is every
positive integer a term?* This package publishes what is proved, what is
computed, and — plainly — what is still open.

## What is proved

**The sequence is injective.** The Row-Triple Theorem: any backward trace
terminating at row i* ≥ 4 lands in {3i*−4, 3i*−3, 3i*−2}; the triples are
disjoint, and the reverse step is deterministic — so each value occurs at
most once. Full proof in `kimberling_complete_paper.md`.

## What is computed

A deterministic reverse-path decision procedure locates, for any value v,
the unique n with a(n) = v when the path reaches the diagonal. Applied to
the 30 positive integers absent from the first 100,000 terms:

- **30 of 30 located** — `located_values.csv`, including 68 = a(181393) and
  669 = a(653494691), the largest located index n = 653,494,691
- **591 of 591** row-triple targets for i* = 4..200 hit the diagonal

## Verification

- Each located value was verified by the reverse-path construction in the
  paper; the recursion itself reproduces all 20 published initial terms.
- Independent forward recomputation (a second implementation of the
  backward trace, run 2026-10-22): a(181393) = 68, a(168343) = 150,
  a(471122) = 384, a(4574186) = 427 — all exact.

## What is still open

**Surjectivity is not proved.** Locating 30 of 30 missing values is strong
computational evidence, not a proof that every reverse path reaches the
diagonal. The $300 problem remains open; `surjectivity_framework.md` records
the forward/contraction direction where a proof is expected to live.

## Files

- `located_values.csv` — the 30 (value, index) pairs
- `kimberling_complete_paper.md` — proof, procedure, full results
- `kimberling_injectivity_paper.md` — the injectivity paper
- `surjectivity_framework.md` — the open direction
- `SHA256SUMS.txt` — checksums for every file in this folder
