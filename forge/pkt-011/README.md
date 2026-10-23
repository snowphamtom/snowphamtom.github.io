# meet-seed fix — DRAWING_ROOM — prepared 2026-10-14

## Diagnosis (verified against live GitHub API, 2026-10-14 ~14:35 UTC)

Run #20 failed today 2026-10-14 12:18:05Z (job 115847725137). Step-by-step from the
jobs API:
- checkout, setup-python, cpu torch install, "harvest + train" all SUCCEEDED
  (train step ran 12:18:36 → 12:18:40).
- "commit ledger if changed" FAILED in 0 seconds (12:18:40 → 12:18:40).

Root cause: the git step runs
`git add artifacts/meet_last.txt artifacts/meet_ledger.jsonl artifacts/corpus.txt`,
but two of the three files never exist:
- `harvest_corpus.py` DOES write `artifacts/corpus.txt` (verified in source).
- `meet_lm.py` writes NOTHING — it only prints to stdout (params, step losses,
  sample, refused_steps). Verified by reading the full 171-line script.
- Nothing anywhere writes `artifacts/meet_ledger.jsonl`.
- The repo's `artifacts/` dir contains only `.gitkeep` (verified via contents API).

So `git add` exits `fatal: pathspec 'artifacts/meet_last.txt' did not match any
files`, bash `-e` aborts the step instantly. This has failed all 20 scheduled
runs the same way — the train always "succeeds" but produces no artifacts, so
the daily seed ledger the cron was built to keep has never been written.

## The fix (two files)

1. `meet_lm.py` — at the end of `main()`, before `return 0`, write the two
   missing artifacts:
   - `artifacts/meet_last.txt`: sample text, refused_steps, used_steps,
     final_loss, params (overwritten each run).
   - `artifacts/meet_ledger.jsonl`: one JSON line appended per run
     (ts, steps_cap, used_steps, final_loss, refused_steps, params).
   Needs the three added imports (json, time, pathlib.Path).
2. `.github/workflows/meet.yml` — one line: make the `git add` tolerant
   (`2>/dev/null || true`) so a missing file can never fail the step again.
   With the script fixed, the add always matches; this is belt-and-suspenders.

## Apply

Copy `meet_lm.py` over `scripts/meet_lm.py` and `meet.yml` over
`.github/workflows/meet.yml` in snowphamtom/DRAWING_ROOM, commit, push.
Or apply `meet_lm.patch` / `meet_yml.patch` with `patch -p1`.
Next scheduled run (06:37 UTC daily) will train, write the ledger, and commit it.

Files here:
- `meet_lm.py` — full patched script (syntax-verified with py_compile)
- `meet.yml` — full patched workflow
- `meet_lm.patch`, `meet_yml.patch` — unified diffs of the same changes
