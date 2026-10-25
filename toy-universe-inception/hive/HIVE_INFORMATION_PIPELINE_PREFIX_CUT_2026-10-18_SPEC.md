# HIVE INFORMATION PIPELINE — PREFIX CUT — SPEC

Video: `HIVE_INFORMATION_PIPELINE_PREFIX_CUT_2026-10-18.mp4`
Sidecar: `HIVE_INFORMATION_PIPELINE_PREFIX_CUT_2026-10-18_BINDING.json`
Renderer: `~/workspace/hive_video/render_hive_prefix.py` (extension of
the prior cut's `render_hive_video.py`, which is untouched; the prior
cut video and its sidecars are untouched). Parser crew output:
`~/workspace/hive_video/prefix_handoff_pairs.json` (read-only).
Judge base: `~/workspace/hive_video/judge_pairs.json` (prior cut).
Deterministic, stdlib + Pillow + ffmpeg. No AI-generated video was
used: a generated video cannot guarantee that every thread is a
counted pair, so the accurate route is deterministic rendering
from counted sources.

## What this cut is

This cut extends the prior cut
(`HIVE_INFORMATION_PIPELINE_FULLY_ACCURATE_2026-10-18.mp4`) with the
15:00 prefix handoff log only. It keeps the prior cut's sections,
format discipline, layout formula, thread-curve math, 2x
supersampled threads with LANCZOS downscale, and defect fixes
(no S5 overflow, no label/timeline collisions, no half-line log
panels, no node-label slivers past card edges). One deliberate
change to a prior-cut card: S4 card 6 now marks the daytime
208-row figure "NOT here" and adds "Prefix here: 45 rows to
15:02 only", so no section of this cut can be read as claiming
full-day coverage.

## Coverage statement (verbatim, also on screen in closing card 2)

"This is a PREFIX cut covering the handoff log only to 15:00
(45 rows, last seq 45, last timestamp 15:02 on Oct 18). The
full-day 208-row density to 18:09:54 is NOT reached in this
material. judge.md is not in this material."

No full-day density is claimed anywhere in this video. The
208-row figure appears only as a NOT-reached / NOT-here marker
(S4 card 6, closing card 2) and as the prior cut's separate
START_HERE snapshot context.

## Coordinator rulings applied exactly

1. THREAD RULE (stated on screen in the replay section header,
   and in the replay log): every listed recipient on every row =
   1 thread. 39 single-recipient rows = 39 threads; 4 broadcast
   rows x 7 = 28 threads; 2 multi-recipient rows = 5 threads
   (seq 31: VERIFIER/SYNTHESIZER/DESTROYER = 3; seq 45:
   CRYPTOGRAPHER/FORMAL JUDGE = 2). Total prefix threads 72.
   ALL HUBS is rendered as the 7 named hubs in the file:
   VERIFIER, EXPERIMENTALIST, MUTATOR, CRYPTOGRAPHER,
   SYNTHESIZER, DESTROYER, FORMAL JUDGE (FORMAL JUDGE drawn to
   the JUDGE node). "ALL 7 HUBS" (seqs 15, 25) and "ALL HUBS"
   (seqs 36, 41) are both rendered as that 7-fan-out.
   SEREPHIM compose worker (seq 32) is drawn as a loop at the
   SEREPHIM node: still one counted thread, sender = recipient.
2. ORDERING (merge): the judge stream (file order, as in the
   prior cut) and the handoff stream (sequence order) are merged
   by walking both streams in their canonical order and emitting
   the head with the earlier timestamp at each step; ties go to
   judge first. Each stream's internal order is preserved. The
   log's two timestamp inversions are kept in sequence order,
   NOT re-sorted, and are noted on screen in the replay log
   ("seq order kept: 14:41>39, 14:50>49"): seq 14 at 14:41
   followed by seq 15 at 14:39; seq 24 at 14:50 followed by
   seq 25 at 14:49.
3. NO OVERLAP: the base's 7 fan-out threads come from the
   separate 18:09 START_HERE handoff (seq 208), not from these
   prefix rows. They are counted once, in the base 116.

## Thread arithmetic (all numbers shown)

- Base (prior cut, unchanged): 116 = 90 judge + 19 path + 7 fan-out.
  - Judge: 90 mapped pairs (92 pairs total, 2 unmapped
    "Recorder" pairs counted, not drawn).
  - Path (REPORTED, baseline video): 19.
  - Fan-out (START_HERE seq 208, 18:09:54): 7.
- Prefix (this cut): 72 = 39 single + 28 broadcast + 5 multi.
- TOTAL DRAWN THREADS: 188 = 116 base + 72 prefix.
- Replay events: 217 = 172 judge entries + 45 prefix rows.
  (Events are not threads: 144 judge entries have no to-field
  and draw no thread; the last mapped judge thread is drawn
  well before the last judge entry, which is why the replay log
  reaches 90/90 judge threads before event 217.)
- Prefix recipient sums, split as listed in the file:
  DESTROYER 8, CRYPTOGRAPHER 7, VERIFIER 7, FORMAL JUDGE 6,
  MUTATOR 6, EXPERIMENTALIST 5, SYNTHESIZER 4, ALL 7 HUBS 2 rows,
  ALL HUBS 2 rows, SEREPHIM compose worker 1 row.
  (39 + 4 + 2 = 45 rows.)
- Prefix thread sums, expanded by the thread rule (each broadcast
  row adds 1 thread to each of the 7 hubs):
  DESTROYER 12, VERIFIER 11, CRYPTOGRAPHER 11, MUTATOR 10,
  FORMAL JUDGE 10, EXPERIMENTALIST 9, SYNTHESIZER 8,
  SEREPHIM compose worker 1. Sum 72.
- Prefix rows: sender SEREPHIM (KING BEE) on all 45 rows;
  first timestamp 2026-10-18T14:35:00-05:00, last timestamp
  2026-10-18T15:02:00-05:00 (seq 45). Sequence contiguous 1-45.
- Timeline strip: 217 ticks, one per merged replay event,
  positioned by that event's own timestamp (gold = judge,
  blue = prefix), spanning 14:35 to 18:11 CT (prefix first
  14:35, judge last 6:11 PM). The count "217 ticks combined"
  is stated in the replay log. The playhead follows the current
  event's timestamp, so it steps back at the two noted
  inversions; that is the disclosed consequence of keeping
  sequence order, not an error.

## Grades used on screen

- VERIFIED: prefix handoff threads (from the extracted log in
  this material); judge parse counts and errata items, as graded
  in the prior cut.
- REPORTED: path threads (baseline video; underlying evening
  file not held); register 11/14/8 at 4:08 PM CT.
- RECORD: register 14/14/5 end of day (2026-10-19 house note).
- NOT CHECKABLE: HI-SCORE JDG 279 rows; JDG hub row text;
  what fantasy/tmp touched.
- Prior-cut grades are carried unchanged (D10 HOLD + writer
  authority unchecked VERIFIED; L4 7,440 as formula output, not
  measurement; witness procedurally compared, not authenticated).

## Layout and rendering formulas (no hand-placed values)

- Frame 1080x1920, 30 fps, black #000000 field, mono type
  (DejaVu Sans Mono), gold #ffd94a / blue #57c8ff / white.
  No glow, no bloom, no blur anywhere.
- Stations: SEREPHIM at frame centre (540, 845). The other 11
  stations on an ellipse, rx 410 px, ry 500 px, angle_i =
  -90deg + i x (360/11)deg in roster order
  (OVERWATCH, BUILDER, VERIFIER, DESTROYER, CRYPTOGRAPHER,
  JUDGE, HERMES, CAULDRON, SYNTHESIZER, EXPERIMENTALIST,
  MUTATOR). Node dots stay at formula positions; label boxes
  are measured with font metrics and clamped to a 12 px frame
  margin. In card sections (S4, S5) nodes are not drawn, so no
  label fragment shows past a card edge.
- Thread curve: quadratic bezier, 48 segments, control =
  midpoint + normal x (0.25 x chord), normal bowed away from
  frame centre. Judge thread colour = linear interpolation
  BLUE to GOLD by entry timestamp. Prefix threads solid BLUE.
  Path threads GOLD (4 px at 2x), judge/prefix threads 2 px at
  2x, fan-out WHITE 2 px at 2x. Self-loop (seq 32) = ring at the
  SEREPHIM node.
- Threads are drawn at 2x (2160x3840) and downscaled with
  LANCZOS for anti-aliased lines; text is rendered natively.
- Smallest text 40 px = 2.08% of 1920 px frame height.
- Log panel shows whole logical lines only (no half-line at
  the top when scrolling); the replay log is exactly 7 lines
  (header facts + current event + thread counts).
- S3 dimming: judge + prefix + fan-out field alpha scaled to
  30% (rendering only, stated on screen); path threads stay full.
- Sections (frames, 30 fps):
  - S1 cold open: frames 0-299 (0-10 s; path stages at
    0.5, 2.0, 3.5, 5.5, 7.0, 8.5 s).
  - S2 merged replay: frames 300-2035 (10.0-67.87 s;
    event k at frame 300 + 8k, 217 events x 8 frames).
  - S3 filter: frames 2036-2485 (67.87-82.83 s).
  - S4 truth locks: frames 2486-2905 (82.87-96.83 s;
    8 cards, card ci = min(7, (frame - 2486) x 8 // 420)).
  - S5 closing: frames 2906-3269 (96.87-109.0 s;
    card 1 counts frames 2906-3087, card 2 prefix coverage
    frames 3088-3269).
  - Frames are composited once per distinct state and reused
    byte-identically for repeated frames.
- Encode: H.264, yuv420p, CRF 14, preset slow, faststart,
  30 fps, no audio track.
- Card-height guard in the renderer (runs before any frame is
  rendered): every card, with its real title and wrapped body,
  must sit between y252 (below the HUD) and y1405 (above the
  timeline strip at y1420). This guard caught a real defect in
  the first prefix render (see below) and now uses real titles
  after the first version of the guard used placeholder titles
  and missed it.

## What this cut does not do

- It does not reach, render, or claim the full-day 208-row
  handoff log to 18:09:54. Only rows seq 1-45 (to 15:02) are in
  this material.
- It does not use judge.md; judge.md is not in this material.
- It does not re-grade the prior cut's REPORTED path threads;
  they stay REPORTED.
- It does not invent rows, recipients, or edges: every drawn
  thread traces to a parsed prefix row (prefix_handoff_pairs.json)
  or to the already-graded base (judge/path/fan-out).
- Nothing was pushed live, sent, or written to the site repo
  by this build. The prior cut file and its sidecars are
  byte-unchanged (prior SHA re-verified after this render).

## Frame inspection (delivered file)

Frames visually checked across all sections (frame numbers
are 0-indexed). First-render pass: S1 frame 255; S2 frames
420 (prefix broadcast seq 15), 588 (multi seq 31), 596
(self-loop seq 32), 708 (last prefix row seq 45), 900, 1500,
2035 (last replay event); S3 frame 2200; S4 frames 2486
(card 1), 2746 (card 5), 2850 (card 7); S5 frames 3000
(card 1), 3200 (card 2, coverage wording). Delivered-file
re-check pass (after the fixes below): S2 frames 420, 588,
708; S4 frames 2538 (card 1), 2590 (card 2), 2642 (card 3),
2670 (card 4), 2798 (card 6, amended), 2900 (card 8);
S5 frame 3000 (card 1). S1, S3, S4 cards 1/5/7 and S5 card 2
are pixel-identical between the two renders (their inputs
were untouched by the fix pass: S1 stages, S3 log, S4 cards
and dim field, S5 card 2); only S2 log event lines and the
S5 card 1 title changed, and those were re-checked from the
delivered file.
Defects found and fixed before delivery (no known visual
defect remains):
1. S2 event line truncated with a dangling "->..." (first
   render, e.g. frames 420/588/708): the event label was
   truncated to 40 characters after a long prefix. Fixed by
   shortening the label format ("52/217 PREFIX seq 45
   2 recipients"; judge lines show the short time, e.g.
   "76/217 JUDGE 3:32 PM") so every event line fits on one
   log line with no truncation; re-rendered and re-checked
   at frames 420, 588, 708.
2. S5 closing card 1 title wrapped to two lines and the card
   bottom covered the top of the timeline ticks (first render,
   frame 3000). Fixed by shortening the card title to
   "CLOSING 1 - COUNTS WITH GRADES" (one line) and by fixing
   the renderer's card-height guard to use the real card
   titles (its first version used placeholders and missed
   the wrap); re-rendered and re-checked at frame 3000, where
   the card now clears the timeline strip with the full
   timeline visible below it.
3. Guard bug itself (above): the first guard used placeholder
   titles "C1"/"C2"; corrected to the real titles and the
   bottom limit tightened to y1405.
After the fixes: no overflow, no label/timeline collisions,
no half-line log panels, no node-label slivers past card
edges in any checked frame. The dimmed thread field visible
around S4/S5 cards is the prior cut's design (dimmed field +
bright path), not a defect: no text is obscured by it.

## Final output measurements

- H.264, 1080x1920, 30 fps, 3270 frames, 109.000 s,
  4,664,987 B,
  SHA-256 acff02621eb6bcbfbde86e94ef957b53db08d05bcd2e7239aebc55676f9a2a1e.
  No audio stream. yuv420p, CRF 14, preset slow, faststart.
  235 distinct composites (S1 7 + S2 217 + S3 1 + S4 8 +
  S5 2), reused byte-identically for repeated frames.
  Render exit 0.
- This file supersedes the intermediate first prefix render
  (4,634,132 B,
  SHA-256 cadc7a901bb1fbd3e91de5be196250e0952d191fc3e55bdc7e85c1b6819b4a93;
  same sections and frame counts, but with the two defects
  above). Only the final file above is delivered.
- Prior cut re-verified unchanged after this render:
  4,414,164 B,
  SHA-256 e87a7b5a3c194a409c177f0152b920a4036a713e29e8d045ab4384520be2ec12.
