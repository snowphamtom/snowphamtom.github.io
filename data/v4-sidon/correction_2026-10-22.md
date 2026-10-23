# CORRECTION — V4 Sidon certification status

**Issued:** 2026-10-22, by Jett at Taylor Heller's direction.
**Supersedes:** the headline "69184/69184 CERTIFIED, 0 alias" in `README_V4_SIDON_69184_CERTIFIED` (Drive folder `V4_Sidon_69184_Certified`) and every swarm product that repeats it.
**Verification basis:** independent rebuild and recomputation, 2026-10-20, two counting methods in agreement (`verify_v4.py`, `verify_v4_detail.py`). The README's claims were treated as unverified until recomputed; the README itself is a third-party artifact (authored "Meta AI for Katie").

## Scope — read this first

This correction applies to ONE matrix: the GF(2^7) construction in the CERTIFIED package — 48 masks, each mask = (x^3 << 7) | x over GF(2^7) with polynomial 0x83 (x^7 + x + 1, primitive).

It does NOT apply to the F_64 set in the CONSOLIDATED DRAFT v3 spec ((x, x^3) construction). That is a different matrix; it was verified separately (69,184 of 69,184 triple patterns refused) and is not corrected here. Do not merge the two records.

## What was claimed

"69184/69184 CERTIFIED, 0 alias" — i.e., all 69,184 signed weight-≤3 syndromes distinct, triple level closed.

## What was measured

### Verified exactly as claimed

- 48 masks, all distinct, nonzero, 14-bit. Row sums (bit 0 = row 1): [31, 25, 22, 28, 20, 26, 27, 28, 23, 25, 25, 26, 22, 19]; total set bits 347.
- Minimum pairwise Hamming distance between masks: 2.
- GF(2^7) polynomial 0x83 is primitive: x has order 127.
- Mask structure: 48 of 48 masks equal (x^3 << 7) | x for 48 distinct nonzero field elements.
- Singles: 48 of 48 distinct, none zero.
- XOR-Sidon: 1,128 of 1,128 pair XORs distinct, none zero, none equal to a single.
- Pairs ++ (integer sum): 1,128 of 1,128 distinct; 0 zero, 0 axis-aligned, 0 collisions with singles.
- Pairs +− (ordered difference): 2,256 of 2,256 distinct; 0 axis-aligned; 0 collisions with singles or ++ pairs.
- No signed pair or triple sum is zero; no triple sum is axis-aligned.
- **The pair level is closed. It is perfect under a stronger count than the README claimed.**

### FAILS — the triple level is NOT closed

- Triples +++: 17,296 sums, 17,286 distinct → **10 collisions**.
- Triples ++−: 51,888 sums, 51,798 distinct → **90 collisions**.
- Cross-weight aliases (a triple syndrome equal to a pair syndrome): **10**. A decoder that repairs by syndrome lookup would repair these wrongly.
- Total aliasing syndromes: **110** (100 within-triple + 10 cross-weight).
- **Distinct triple syndromes: 69,084 of 69,184.**
- Worst cluster: columns **{19, 36, 38, 41, 45}**. Triple (19, 38, 41) equals pair (36, 45) as integer vectors; that one identity spawns 9 derived ++− aliases inside the same 5-column set.

## Corrected statement — use this wording

> Pair level closed (1,128/1,128 pair sums, 2,256/2,256 ordered differences, XOR-Sidon clean). Triple level not closed: 69,084 of 69,184 triple syndromes distinct (10 +++ collisions, 90 ++− collisions, 10 cross-weight aliases). The label "69184 CERTIFIED" is withdrawn.

Do not cite "69184/69184", "69184 CERTIFIED", or "0 alias" for this matrix in any product, deck, ledger, or app.

## Swarm products carrying the withdrawn headline — correct the label in each

- Sidon_Hive iPhone/web3 apps (AutoLoad Baked; Full Demo Baked; Web3 iPhone) and their Google Doc copy — includes the MetaMask wallet-sign "69184/69184 OWNERSHIP" flows.
- LightBurn 4x6 grid project.
- PC runner (.html + .bat).
- Split-zip bundle "MASTER_13_VARIANTS_69184_CERTIFIED".
- "Gemini Export October 20, 2026 at 5:06:30 PM CDT" doc declaring every file "VERIFIED" (a Gemini summary is not independent verification).
- Evidence Ledger entry "03_EVIDENCE_LEDGER_17_BATTERIES - 69184 Triples PASS" (2026-10-15) — the "Triples PASS" line is the same overclaim.

Note: the swarm headers citing "H14 rows 10-14: 23,25,25,26,22,19" are quoting rows 9–14 of the verified row sums — a labeling slip; the matrix underneath is the one verified above.

## What stands

- The corrected record already exists and is canonical: `~/workspace/v4_verify_2026-10-20/RESULTS.md` and the Phygital Record (Drive folder "V4 Sidon — Phygital (complete)"), which carries the measured table and marks columns 19, 36, 38, 41, 45 red in both the physical plates and the digital twin.
- Unresolved and not part of this correction: the "seed6" selection rule for the 48 x-values.
