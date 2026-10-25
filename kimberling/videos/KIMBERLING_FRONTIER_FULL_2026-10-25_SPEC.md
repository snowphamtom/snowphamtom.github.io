# SPEC — KIMBERLING FRONTIER FULL (v5, final)

- File: KIMBERLING_FRONTIER_FULL_2026-10-25.mp4 (live name drops the _v5)
- SHA-256: 402719b89b317ca2c6aeda7de7cb9ad8bef428ee29d40b8efd2c492a4e69eb4e
- Size: 4,251,186 B. Codec: H.264, yuv420p, CRF 14, preset slow, faststart.
- Format: 1080×1920, 30 fps, 2,880 frames, 96.000 s, no audio.
- Type: DejaVu Sans Mono, gold #ffd94a / blue #57c8ff / white on black
  #000000, no glow, no blur. Smallest text ~40 px.

## Sections

- S1 (frames 0–239): the sweep stated — 29,965 of 29,991 admitted,
  26 capped, rows 4–10,000, 3 targets per row, zero rows with ≠3,
  max n = 4,733,484,458, total steps 278,075,290,444 (hit-only
  148,075,290,444). "Every target plotted. Nothing sampled."
- S2 (frames 240–1559): the full map revealed row by row — x = row,
  y = log10(n), gold hits, blue capped band at top, n = 50,000 line,
  white ring on the max point, live counter. Final frame: "row 10000
  of 10,000 · 29991 targets drawn" + MAX line.
- S3 (after S2): the 26 capped named with deep-walk statuses
  (two cards of 13).
- S4: the shape — 21,059 by n = 50,000; step totals reconciled;
  continuous coverage.
- S5: closing — "CAPPED DOES NOT MEAN DISPROVEN" + sources +
  "FULLY: 29,991 targets plotted, 26 capped named, 0 sampled."

## Data

Merged from the six campaign CSVs (phase1_impl_b, phase2 201–1000,
1001–10000, 4805–10000, 6232–10000.part1, 6666–10000), conflict
aborts, 0 conflicts. 29,991 targets = rows 4–10,000 × 3. Hits 29,965;
capped (hit = 2, n = −1, steps = 5,000,000,000) 26.

## QA (v5)

- S2 frame 900: header, legends, gridlines, capped-band label (below
  the band, no legend overlap), row 10,000 label (right-aligned,
  fully visible), counter "row 5005 of 10,000 · 15006 targets drawn"
  — all clean.
- S2 frame 1559: "row 10000 of 10,000 · 29991 targets drawn" + MAX
  line + white ring on the max point + full-width map + full capped
  band — all clean.
- S1/S3/S4/S5: source frames unchanged since v1 (only S2 frames were
  re-rendered in v2–v5); v1 sampled QA for those sections (frames 0,
  1700, 2200, 2700) was clean and carries over. The v5 encode
  re-encoded all frames at identical settings.
- Superseded versions (not for distribution): v1 (S2 opaque-paste
  defect, disclosed on delivery), v2 (S2 labels fixed, row-10,000
  label overflow), v3 (encode truncated by a service restart,
  unreadable), v4 (killed mid-encode to fold in the denominator fix;
  partial file, overwritten by v5).

## What this video does NOT claim

Surjectivity is OPEN. The 26 capped are UNKNOWN, not disproven, not
refused. The $300 prize is unclaimed.
