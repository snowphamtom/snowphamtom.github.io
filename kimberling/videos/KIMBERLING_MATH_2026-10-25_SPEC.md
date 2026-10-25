# SPEC — KIMBERLING MATH VIDEO (v4, final)

- File: KIMBERLING_MATH_2026-10-25.mp4 (live name drops the _v4)
- SHA-256: e21da4ef28dbc17fe675e648384436a8982b518bb14ab7b1adcf5d3098e6dc0d
- Size: 2,103,564 B. Codec: H.264, yuv420p, CRF 14, preset slow, faststart.
- Format: 1080×1920, 30 fps, 2,880 frames, 96.000 s, no audio.
- Type: DejaVu Sans Mono, gold #ffd94a / blue #57c8ff / white on black
  #000000, no glow, no blur. Smallest text ~40 px.

## Sections

- S1: the K recursion + 20 computed terms (walk.c `terms 20` →
  20/20 match with the published terms).
- S2a: n = 20 backward trace, step by step.
- S2b: ONE REAL WALK, v = 502 — the real reverse-walk trajectory
  (1,190 sampled states, x = log10(row), y = d, white diagonal
  d = 0, blue start marker, gold arrival ring, live sample counter,
  "ARRIVED: a(118,850,522) = 502").
- S3: row triples proved + injectivity (every value at most once).
- S4: the mirror on the real n = 20 forward trace (u_A 62/9 →
  −31/9 contract-and-flip; u_B −32 → −16 → −8 → −4 halving; fixed
  targets −12/−10/−8; switch cost (4/3)i + 29/9; switch stats
  labeled CITED to the campaign's 1,181 instrumented walks).
- S5: BRIDGE stated exactly + $300 unclaimed + 29,965/29,991,
  0 stuck + surjectivity OPEN.

## QA (v4)

- S2b final frame (frame 1079): "sample 1190 of 1,190 · row
  118,850,522", "d = 0", "ARRIVED: a(118,850,522) = 502" in gold
  with the arrival ring; header, diagonal, and row labels all
  visible — clean.
- Two-line counter format (line 1 "sample K of 1,190 · row R",
  line 2 "d = D", ARRIVED moved clear): verified on v3 frame 800
  ("sample 397 of 1,190 · row 39,600,169" + "d = -37,570,744"
  fully visible). v4 changes only the reveal denominator (420 →
  419), shifting mid-section sample numbers by at most 1 and
  fixing the final frame to sample 1190 (verified on v4 frame
  1079 above). No v4 mid-section frame number is claimed here
  beyond that bound.
- S1/S2a/S3/S4/S5: source frames unchanged since v1 (only S2b
  frames were re-rendered in v2–v4); v1 sampled QA for those
  sections was clean and carries over. The v4 encode re-encoded
  all frames at identical settings.
- Superseded versions (not for distribution): v1 (S2b opaque-paste
  defect covering header/diagonal/labels, reveal pacing wrong —
  log-x slicing vs linear walk progress, row label overflow;
  defects disclosed on delivery), v2 (RGBA compositing +
  sample-index reveal + right-aligned label, clean except the
  one-line counter overflowed so the d value never showed),
  v3 (two-line counter, frames 800 + 1079 clean, HELD — last S2b
  frame showed sample 1187/1190, arrival never shown).

## What this video does NOT claim

Surjectivity is OPEN. The 26 capped are UNKNOWN, not disproven, not
refused. The $300 prize is unclaimed. The mirror switch stats are
CITED (1,181 walks), not recomputed here.
