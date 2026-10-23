# Sidon Codec Sets — Filed Baseline, the F₆₄ Spec Set, and the r = 10 Set

Taylor Heller / Monsters Ink LLC — published 2026-10-22.

Three 48-column sets, measured exhaustively in the unit-amplitude integer
model by `battery.py` in this folder, run on the exact CSVs published
here. Decoder acceptance models are defined at the bottom; every figure
below names its model.

## filed_55 — the filed [55,8] matrix (U.S. application 64/170,360)

The masks are the odd numbers 3–97 (7 rows; bit 0 set in every column).

- Row sums **[48, 24, 24, 24, 24, 17, 17]**, 178 bits; min distance 1.
- Integer pair sums ++: **464 of 1,128 distinct** — this matrix is *not*
  Sidon, and never claimed the later sets' properties. XOR pair sums:
  63 distinct.
- Weight-3 patterns: 61,888 of 69,184 refused; **7,296 alias into a
  repair class**, the same count under all three acceptance models
  (reproduced by `battery.py`; first measured by the level100_v4.py
  Phase 1 battery).
- This is the filed baseline the sets below evolved from: its documented
  flaw findings (56 of 1,128 equal-magnitude pair aliases in the 6-row
  predecessor [54,8]; 124 of 1,128 in this 7-row matrix, per the
  level100 Phase 1 record) are what the F₆₄ and GF(2⁷) constructions
  were built to eliminate.

## f64_spec — the CONSOLIDATED DRAFT v3 §3.5 set

Construction: ((x, x³) << 2) | 3 over F₆₄, two common bits, 14 rows.
The mask list is the constructor's own output (`construct_v4b.py`,
MASKS4), byte-identical to the spec's printed §3.5 list.

- Row sums **[48, 48, 23, 24, 23, 22, 19, 18, 25, 32, 20, 28, 30, 21]**,
  381 bits; min distance 2.
- XOR pair sums 1,128/1,128 distinct; integer ++ 1,128/1,128;
  ordered +− 2,256/2,256 — pair level closed.
- Triples are **not** distinct: +++ 17,165 of 17,296; ++− 50,761 of
  51,888; 67,926 of 69,184 syndromes distinct. No distinctness is claimed.
- What is claimed, and measured: **refusal**. No triple syndrome is zero,
  a signed column, a signed unit vector, or a pair syndrome — so all
  69,184 weight-3 patterns are refused under Models A, A+, and B:
  **0 accepted**.

## r10 — the minimum measured working row count: 10

A 10-row set (framing B: no common bit, no dead row; column weights 2–8),
located by search and verified exhaustively 2026-10-21.

- Row sums [27, 26, 26, 27, 25, 27, 25, 28, 24, 24], 259 bits;
  min distance 2.
- Integer Sidon exact: ++ 1,128/1,128 distinct; ordered +− 2,256/2,256.
  (Not XOR-Sidon: 743 of 1,128 XOR pair sums distinct — not claimed.)
- Decoder acceptance: **0 of 69,184 weight-3 patterns** under Model A and
  under the amplitude-extended Model A+ — no syndrome is zero,
  axis-aligned, or parallel to any column at any amplitude. Under
  Model B (pair-correcting lookup), 490 patterns land on pair syndromes
  and would be accepted; the admission classifier that was built refuses
  them.
- Triples are **not** distinct: +++ 16,499 of 17,296; ++− 45,601 of
  51,888. Cite this set as a battery pass, never as distinct.
- **r = 10 is the minimum measured working row count. It is not proved
  minimal.** Proved floors: r ≥ 8 (no common bits), r ≥ 9 (one common
  bit), r ≥ 10 (two common bits). r = 8 and r = 9 remain open.

## Acceptance models

- **Model A** — the admission classifier as built in the Verilog decoders:
  accept iff the syndrome is 0, a signed column, or a signed unit vector
  (the tail lane); refuse everything else.
- **Model A+** — Model A with amplitudes e ∈ {±2, ±3} admitted on columns
  and unit vectors.
- **Model B** — a lookup decoder that additionally corrects weight-2
  faults by syndrome.

## Files

- `filed_55_masks.csv` — the filed [55,8] set (odd numbers 3–97)
- `f64_spec_masks.csv` — the F₆₄ spec set
- `r10_masks.csv` — the r = 10 set
- `battery.py` — the exhaustive battery (standard library only)
- `battery_results.txt` — its output on these exact files
- `SHA256SUMS.txt` — checksums for every file in this folder
