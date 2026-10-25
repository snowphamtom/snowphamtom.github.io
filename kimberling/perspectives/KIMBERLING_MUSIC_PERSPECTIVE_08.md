# PERSPECTIVE 8 — MUSIC (built fully)

A playable piece derived from the real v = 502 reverse walk by STATED
rules. The data is real; the mapping is a convention, stated here,
not a discovery. Nothing about the math is claimed from the music.

## The piece

32 bars of 3/4 at 120 BPM, 48.0 seconds. Two voices:

- **Drums (rhythm, EXACT):** the walk's branch sequence. Branch 0 =
  LOW (bass drum, MIDI 36); branch 1 = HIGH (closed hi-hat, MIDI 42).
  One stroke per quarter note, three per bar. The rhythm IS the
  branch sequence — it inverts back to the walk, stroke for stroke.
  First 96 branches of the v = 502 walk:
  111110001101010110111001101111101001110101001100001100001011000001100001000001000011100001101110.
- **Melody (one note per bar, PROJECTION):** 32 evenly spaced sampled
  states from the 1,190-point v = 502 trajectory (indices
  floor(i*1189/31), i = 0..31), mapped to pitch by a stated rule:
  d = 0 → MIDI 84 (C6, the arrival — highest note, distinct);
  d < 0 → 60 + C-major degree from floor(log10|d|) mod 7 (60–71);
  d > 0 → 72 + the same degree (72–83). The melody is quantized
  and lossy — it does NOT invert back to d. Only the rhythm is exact.

## Why these rules (what is grounded, what is chosen)

- **Triple meter (3/4)** mirrors the proved row-triple partition
  (perspective 3: every value sits in exactly one triple). The meter
  is CHOSEN to mirror that structure; it is not derived from the
  walk steps. Grouping walk steps in threes is a bar, not a theorem.
- **Two-stroke rhythm** is the walk's own binary branch structure
  (perspective 7's coin, made audible). No third stroke exists in
  the walk, so none is invented.
- **Melody from d** uses the trajectory's actual displacement across
  the diagonal (perspective 1's walk, perspective 5's mirror
  variable family). The log-magnitude quantization is a rendering
  choice; a different scale would give a different tune from the
  same walk. The arrival bar resolves to C6 because d = 0 is the
  diagonal — the walk's destination, not a chord choice.
- **Tempo 120 BPM** is arbitrary (a performance choice, stated).

## Verification (all recomputed for this build)

- Engine: `~/workspace/kimberling_video/music.py` (walk ported
  exactly from coin.c; MIDI written by hand, format 0, no library).
- The Python walk's 96 branches match coin.c's `seq 502 96` output
  EXACTLY — two independent implementations agree on all 96.
- Verifier: `~/workspace/kimberling_video/verify_music.py` parses
  the MIDI back and checks it against independent sources:
  **VERIFY OK: 3/4, 120 BPM, 96 drum strokes == coin.c branches,
  32 melody notes == d-rule on traj samples, last = 84 (arrival),
  46080 ticks = 48.0 s.**
- Files: KIMBERLING_SCORE_2026-10-25.mid (1,161 B, playable in any
  MIDI player) + KIMBERLING_SCORE_2026-10-25.txt (the 32 bars, readable).

## The boundary (what "music" does NOT mean)

- NOT a discovery that the math "is" music. The walk does not
  compose; a stated rule renders it as sound.
- NOT evidence for anything about surjectivity, the $300 problem,
  or any other open question. The piece ends at the arrival because
  v = 502 arrives; the 26 capped values have no arrival bar, and no
  bar is invented for them.
- NOT a randomness source (perspective 7's boundary stands): the
  rhythm is fully determined by v.

## What "fully" means for this perspective

The score defined (rules stated, grounded-vs-chosen separated) +
the walk recomputed (96 branches, cross-implementation match) +
the melody derived (32 samples, stated rule, arrival distinct) +
a playable MIDI written and parsed back (all checks pass) +
the boundary stated. Statistics claimed only where measured; the
piece claimed only where rendered.
