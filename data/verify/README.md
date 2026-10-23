# VERIFY_ALL — every claim in the Master Document, as runnable code

Taylor Heller / Monsters Ink LLC, 2026-10-22.

`VERIFY_ALL.py` is a single-file, Python-3-standard-library verifier for
the claim set of *Monsters Ink LLC — Master Document (2026-10-22)*. It
does not ask to be trusted: it recomputes. Every check prints the CLAIM
and the MEASURED value and reports PASS, FAIL, SKIP, or RECORD.

    python3 VERIFY_ALL.py            # full run (several minutes: the
                                     # largest Kimberling trace is
                                     # 653,494,691 diagonal steps)
    python3 VERIFY_ALL.py --fast     # skips the three largest traces
    python3 VERIFY_ALL.py --spectral # also re-runs the spectral scripts

Exit code = number of FAILs (0 = clean).

## Result of record (author's machine, 2026-10-22)

**215 PASS / 0 FAIL / 1 SKIP / 13 RECORD** — full output in
`verify_results.txt`. The one SKIP is the spectral section (not selected
in that run; its scripts and fresh outputs live in the spectral drop).
The suite has already earned its keep: its first run caught an error in
the Master Document itself (the filed code's minimum distance, since
corrected in the document, not in the test).

## What runs anywhere, and what needs the author's workspace

- **Self-contained (runs on any machine):** every codec battery — the
  filed [55,8] set, the F₆₄ specification set, the GF(2⁷) seed6 set and
  its certification withdrawal, the fully closed GF(2⁷) set, the r = 10
  set, the regenerated dual-mirror set — under the published acceptance
  models A / A+ / B; all 30 Kimberling located pairs, forward-traced
  end-to-end; the money identities.
- **Workspace-bound:** checks whose evidence lives in the author's
  workspace (the Drive census manifest, the content-sweep outputs, the
  swarm register, the published-drop trees, receipt-hash anchors). When
  a file is absent the check SKIPs and prints the path it looked for —
  it never guesses. Set `MUSE_WORKSPACE` to point at a mirror.
- **RECORD items** are claims that are records rather than computations
  (receipts, meeting facts, submission states, proof-only claims). The
  suite enumerates all of them with their evidence pointers, so every
  claim in the document is accounted for: recomputed, or named as a
  record with the evidence it rests on.

The rule the suite implements is the record's own: a claim is admitted
only if it fits inside what an independent machine can recompute;
otherwise it is refused, or labeled with exactly what it rests on.
