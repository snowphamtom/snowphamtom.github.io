# HIVE INFORMATION PIPELINE — FULLY ACCURATE CUT — SPEC

Video: `HIVE_INFORMATION_PIPELINE_FULLY_ACCURATE_2026-10-18.mp4`
Sidecar: `HIVE_INFORMATION_PIPELINE_FULLY_ACCURATE_2026-10-18_BINDING.json`
Renderer: `~/workspace/hive_video/render_hive_video.py` (deterministic,
stdlib + Pillow + ffmpeg). Parser: `~/workspace/hive_video/parse_judge.py`.
No AI-generated video was used: a generated video cannot guarantee
that every thread is a counted pair, so the accurate route is
deterministic rendering from counted sources.

## Baseline measured (not estimated)

- Baseline video (user upload, 2026-10-25): HEVC 720x1280, 30 fps,
  2250 frames, 75.000 s, 18,179,286 B, AAC audio,
  SHA-256 1613909ef5728bc1e5347d95a4477d33a5f8eb43832fac23df69b5b176af7f3d.
- Portrait intricacy reference (user upload): JPEG 420x630, 57,286 B,
  SHA-256 75b7b4b0538cf6044495b8f0c9b49ffb015766da1cad1131598db46b4c2c1dc6.
  "Portrait ethnique du Canada" (UQAM). Its role is density grammar
  only (many fine threads, black field, top sources to bottom
  destinations); none of its data is used.

## Held sources (everything drawn or stated comes from these)

- `drive_audit/dl_judge_rulings_2026-10-18.md` — requests.md extract,
  snapshot SHA-256 acaab0648ebd60c6f1897ca4d0fb3aa5d502a01399040c9ea13e3b205a47e6f4
  (quoted in the file header), 2078 lines, extracted 6:17 PM CT.
  File SHA-256 4e0730d561f1a50e021f439e61510c69d2d0d5139f6a7c117c76096dc581f2e1.
- `drive_audit/START_HERE.md` — HIVE relay export, snapshot 2026-10-18
  about 18:13 CT. File SHA-256 c209ae5d9c8cc0609ae3442de2327630f3c67fdf043de0ff9a97267956f65e94.
- `drive_audit/HIVE_fantasy_ERRATA_2026-10-18.md` — Overwatch errata
  for the fantasy cut. File SHA-256 b0a542532d042bf64c9dec61746a065051bb54f2f38c67451c1a9ad0192f671c.
- Baseline video itself (above) — carried only as REPORTED, never
  upgraded to verified, because the evening handoffs file it replays
  is not held in this workspace (see below).

## Counted datasets (parser output: hive_video/judge_pairs.json)

- Judge entries parsed: 172 dated entry headers, in file order,
  timestamps 2026-10-18 2:36 PM CT to 6:11 PM CT (span 215 minutes),
  time order inversions 0. File header claims 175 entries.
  Reconciliation: 172 dated + 1 undated trailer line (requests.md
  l.2074, kept with the 6:11 PM block) = 173; delta 2 entries
  unaccounted for in the extract as held — UNRESOLVED, and 175 is
  never cited as verified in the video.
- Withheld content lines: 67 (matches the header claim; the header
  prose line mentioning [withheld] is excluded from the count).
- Entries with a to-field: 28. Entries without a to-field: 144.
- Pairs: 92 total = 90 mapped + 2 unmapped. Unmapped recipient
  string: "Recorder" (2 pairs) — a role, not a station node;
  counted on screen, drawn to no node.
- Mapped recipient counts: SEREPHIM 20, VERIFIER 17, DESTROYER 13,
  MUTATOR 11, SYNTHESIZER 10, CRYPTOGRAPHER 8, EXPERIMENTALIST 8,
  OVERWATCH 3. Sum 90.
- Drawn threads, total 116 = 90 judge + 19 path + 7 fan-out.
  - Judge (VERIFIED parse): one thread per mapped pair,
    JUDGE node to recipient node.
  - Path (REPORTED, baseline video): BUILDER to SEREPHIM 1,
    SEREPHIM to QA four (VERIFIER, CRYPTOGRAPHER, DESTROYER,
    EXPERIMENTALIST) 4, QA four to JUDGE 4, JUDGE to SEREPHIM
    PASS 1, SEREPHIM to HERMES 1, HERMES to all7 + Overwatch 8.
  - Verified fan-out: one VERIFIED handoff (START_HERE snapshot,
    handoffs seq 208, 18:09:54 CT, SEREPHIM to all7, "KING BEE S1
    stop rule; Destroyer BREACH medium"), rendered as fan-out
    to the 7 seats (7 threads). Rendering rule stated on screen.
- Timeline strip: 172 ticks, one per parsed entry, positioned by
  the entry's own timestamp (linear map across the strip).
- No decorative threads. No haze, no dust. (The baseline had
  decorative haze/dust; this cut removes it so that every line
  on screen is a counted pair.)

## Grades used on screen

- VERIFIED: recomputed from a held file in this build.
- REPORTED: the baseline video's claim, carried with attribution;
  the underlying file is not held here, so it is not upgraded.
- RECORD: a prior house record (not recomputed here).
- NOT CHECKABLE: stated in a source as having no checkable source,
  or no source held. Never presented as a figure.

## Figures and their grades

- D10 HOLD + "writer authority unchecked": VERIFIED. Judge extract:
  DESIGN.rev3 R6 says writer authority is NOT checked and "Any
  D10 label must carry 'writer authority unchecked'" (requests.md
  l.1018 via extract); D10 stays HOLD (extract l.1321 and others).
- L4 7,440: VERIFIED as a formula output, not a measurement.
  Extract: doors.window_max_7440 (HELD, COMPUTED finite) and
  "7,440 is a formula output, not a measurement" (requests.md
  l.233, l.530, l.536, l.548 via extract).
- Witness "procedurally compared, not authenticated": VERIFIED.
  Extract: W3 procedure, "Doc line procedurally compared", never
  "witnessed" or "authenticated" (requests.md l.779 via extract);
  w3 log c47eb715 procedurally compared, not authenticated
  (requests.md l.1330 via extract).
- Register 11 HELD / 14 BROKE / 8 PENDING of 33 at 4:08 PM CT:
  REPORTED (baseline video's as-of figure; the register file
  itself is not in the held pack).
- Register 14 / 14 / 5 end of day: RECORD (2026-10-19 house note).
  Both as-of states are shown; the change between them (3 rows
  PENDING to HELD) is arithmetic on the two stated figures, not
  a re-verification.
- Gate attack rev3.5 (KILL 0, MAJOR 4: Verifier 2, Destroyer 2),
  r2 tests 143/143 (p5 53, anchor 48, s1c 42), VER 38/38 bound
  shas EXACT, CAULDRON 7 CLIs (2 write + 1 optional log):
  REPORTED (baseline video; none located in held files).
- HI-SCORE JDG 279 rows: NOT CHECKABLE (errata item E2).
- Fantasy mp4 SHA-256 (full):
  05602d9d19fe7a846e8944c1a0d20ba427028746aa83346e7ec9f1f5de235a4d
  (errata subject line). BINDING dbc01157 (NOT edited).

## Errata corrections on screen (S4, 8 cards, Overwatch errata)

- E1 event-line clear: the 2.5 s claim is WRONG for 3 of 9 events
  (LEDGER REWRITTEN 2.68 s, f988 to f1148; 15:33 KILL 3.03 s,
  f1966 to f2147; 15:08 ANCHOR 1.57 s early, f1856 to f1949).
  Escalated m5 line (15:49:07) FIXED at 2.50 s (Judge). Builder
  timed from the end of the typing script, not the last glyph.
- E2 score text: NOT dropped. 'HI-SCORE JDG 279 rows', HIGH SCORES
  board and SCORE formula remain on screen; 279 NOT CHECKABLE;
  28 dropped strings decorative (Destroyer 6734d57b).
- E3 missing locks: M1, M1b, M2, JDG hub row and both
  witness-own-time locks absent from locks.json (scanner coverage
  gap, MUST-FIX). MA2 absent by design (not applicable). JDG hub
  row text NOT CHECKABLE.
- E4 TMPDIR: BINDING l.37 sets TMPDIR=fantasy/tmp; earlier
  disclosure 2f8d480d omitted it; fantasy/tmp touch at
  22:17:11.817 most likely the builder's; what was touched NOT
  CHECKABLE. QA-probe hypothesis WITHDRAWN.
- E5 generator chmod 0444 logged, but chmod-before-render not
  demonstrated: CLOSE.
- CLOSE items: HOLD badge contrast 8.88:1 measured by Exp (builder
  claimed 9.2:1; still above 7:1). 24 SCAN orphans are real typing
  partials, not false positives (Judge: CLOSE). BINDING has no
  disclosures key (next cut adds one).
- File-version note (S4 card 6): daytime handoffs snapshot is
  208 rows to 18:09:54 CT (START_HERE; file SHA-256
  f09ccfd4a48f64365086c9dd059892e65556356dd1271578d8fc62e74171af13
  as quoted in the export). The baseline's evening replay lines
  :233 to :350 (18:51 to 23:07) come from a later version of
  handoffs.jsonl that is NOT HELD in this workspace. The video
  never presents the two versions as one file.

## Layout and rendering formulas (no hand-placed values)

- Frame 1080x1920, 30 fps, black #000000 field, mono type
  (DejaVu Sans Mono), gold #ffd94a / blue #57c8ff / white.
  No glow, no blur, no shadowBlur anywhere.
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
  BLUE to GOLD by entry timestamp. Path threads GOLD (4 px at
  2x), judge threads 2 px at 2x, fan-out WHITE 2 px at 2x.
- Threads are drawn at 2x (2160x3840) and downscaled with
  LANCZOS for anti-aliased lines; text is rendered natively.
- Smallest text 40 px = 2.08% of 1920 px frame height.
- Log panel shows whole logical lines only (no half-line at
  the top when scrolling); bodies are truncated on screen with
  an explicit note that full text is in the source file.
- S3 dimming: judge + verified field alpha scaled to 30%
  (rendering only, stated on screen); path threads stay full.
- Sections: S1 cold open 0-10 s (path stages at 0.5, 2.0, 3.5,
  5.5, 7.0, 8.5 s); S2 replay 10-55 s (172 entries in file
  order, entry k at frame 300 + (k x 1350) // 172); S3 filter
  55-70 s; S4 truth locks 70-84 s (8 cards, card ci =
  min(7, (frame - 2100) x 8 // 420)); S5 closing 84-96 s.
  Frames are composited once per distinct state and reused
  byte-identically for repeated frames.
- Encode: H.264, yuv420p, CRF 14, preset slow, faststart,
  30 fps, no audio track.

## What this cut corrects against the baseline

1. Adds the Overwatch errata (E1-E5 + CLOSE items) — the baseline
   carries none of them.
2. Grades every figure (VERIFIED / REPORTED / RECORD /
   NOT CHECKABLE) — the baseline presents all figures under a
   single "real logs only" stamp.
3. Replaces the baseline's single-file replay implication with
   the file-version truth: daytime snapshot 208 rows vs evening
   lines :233-:350 from a later, not-held version.
4. Replaces the baseline's decorative haze/dust with zero
   decorative threads: every line is a counted pair.
5. Replaces the header claim 175 with the reconciled count:
   172 parsed + 1 trailer = 173, delta 2 unresolved.
6. Keeps the baseline's verified lines intact (D10 HOLD +
   writer authority unchecked; L4 7,440 as formula, not
   measurement; witness procedurally compared) with citations.

## Unresolved items (stated, not hidden)

- Entry-count delta 2 (175 claimed vs 173 accounted for).
- Evening handoffs.jsonl (:233-:350) not held here.
- Judge register file (judge.md) not in the held pack.
- HI-SCORE 279 rows not checkable; JDG hub row text not
  checkable; what fantasy/tmp touched not checkable.
- Locks M1, M1b, M2, JDG hub row, both witness-own-time locks
  still absent from locks.json (MUST-FIX next cut, per errata).

## Final output measurements

- H.264, 1080x1920, 30 fps, 2880 frames, 96.000 s, 4,414,164 B,
  SHA-256 e87a7b5a3c194a409c177f0152b920a4036a713e29e8d045ab4384520be2ec12.
  No audio stream. yuv420p, CRF 14, preset slow, faststart.
  189 distinct composites (S1 7 + S2 172 + S3 1 + S4 8 + S5 1),
  reused byte-identically for repeated frames. Render exit 0.
- Frame verification (shots extracted from the final file):
  S1 frame 299, S2 frame 1640, S3 frame 1800, S4 card 8 frame
  2480, S5 frame 2700 — all visually checked. S5 closing card
  fits between HUD and timeline/log with every line visible;
  S4 card 8 (recipient distribution) fits; S2 HERMES and JUDGE
  labels clear the timeline strip; S1 log shows whole lines
  only. Threads render smooth (2x supersampling).
- This file supersedes the intermediate fixed cut (3,980,361 B,
  SHA-256 6f57e1ed275726d581f764904741cb5e7eac539006111e99f471cb8951255271;
  CRF 18, 7 truth cards, 1x threads). Only the final file above
  is delivered.
