# STATUS — THE FLOOR ON THE SITE

*Landed 2026-10-23T12:59:08Z under Taylor's directive of 2026-10-23 07:54 CT
("Generate private swarm using my site and GitHub"). This board is
regenerated at each landing.*

## Where the floor lives

**https://sequesteredyeti.art/swarm/** — inside `snowphamtom/snowphamtom.github.io`,
under `swarm/`. Behind its own door (the site's speak-and-be-known pattern),
linked from nowhere public; the wall keeps exactly its two hrefs. Working
Copy reaches the floor through the site repo Taylor already holds — no new
repo, no creation step.

The private `the-swarm` repo of the earlier plan does not exist and the App
cannot create it (403, measured 2026-10-23 — item T3). That plan is
superseded by this landing, struck-but-visible in the kit's staging record
(`~/workspace/swarm_github/` on the VM).

## Register at the landing

- **Rows:** 329
- **Tip:** `fa859918467cb28c4068168ae31291bcbbc915e51a997b8546f8838d5ac2a03c`
- **Chain:** PASS — full chain re-verified at the build (2026-10-23T12:59:08Z)
- **Mirror file SHA-256:** `da75d5e4edba19605937ddccef48f2477a7e79ae540dde2a1770ed2ad14de62d`
- **By kind:** DESIGN_ADOPTED 1 · NOTE 262 · PACKET_ADMITTED 31 · PACKET_REFUSED 5 · POLICY 1 · RECEIPT 16 · SEAT_DECLARED 13

## Seats (from seats.json v1.1, via the kit's manifest)

| Seat | State |
|---|---|
| THE DOOR — the floor's entrance (Taylor's seat-zero) | SEAT ZERO |
| THE REGISTER — the spine (mirror state & chain verification) | THE SPINE |
| [SEAT] SEREPHIM — Dispatch (ORCHESTRA) | LIVE |
| [SEAT] GATE — Admission (ORCHESTRA) | LIVE |
| [SEAT] FLOW — Ledger chain (ORCHESTRA) | LIVE |
| [SEAT] VERIFIER — Recompute (VERIFY) | LIVE |
| [SEAT] JUDGE — Formal rulings (VERIFY) | LIVE |
| [SEAT] CRYPTO — Receipts and hashes (VERIFY) | LIVE |
| [SEAT] FORGE — Code, HDL, sims (BUILD) | LIVE |
| [SEAT] ATELIER — Creative builds (BUILD) | LIVE |
| [SEAT] SCRIBE — Documents (BUILD) | LIVE |
| [SEAT] TINKER — Drive organisation (HOUSE) | LIVE |
| [SEAT] PHONE_ELF — Inbox sorting (HOUSE) | LIVE |
| [SEAT] WARDEN — The watches (HOUSE) | LIVE |
| [SEAT] SCOUT — Market + intel (HOUSE) | LIVE |
| [SEAT] TOLL — Revenue (HOUSE) | LIVE |
| [HIVE] 01 SEREPHIM — Dispatch — HIVE lead | LIVE |
| [HIVE] 02 SG-VERIFIER — Verification | LIVE |
| [HIVE] 03 CRYPTOGRAPHER — Receipts and hashes | LIVE |
| [HIVE] 04 FORMAL-JUDGE — Formal rulings (GRIMM) | LIVE |
| [HIVE] 05 DESTROYER — Adversarial attack | STRUCTURE-ONLY |
| [HIVE] 06 MUTATOR — Variation | STRUCTURE-ONLY |
| [HIVE] 07 EXPERIMENTALIST — Experiments | STRUCTURE-ONLY |
| [HIVE] 08 SYNTHESIZER — Synthesis | STRUCTURE-ONLY |
| [HIVE] 09 SEAT-NINE — UNRESOLVED | UNRESOLVED |

ORCHESTRA: SEREPHIM · GATE · FLOW — VERIFY: VERIFIER · JUDGE · CRYPTO —
BUILD: FORGE · ATELIER · SCRIBE — HOUSE: TINKER · PHONE_ELF · WARDEN ·
SCOUT · TOLL. All 14 LIVE on the VM today.
HIVE wing: SEREPHIM, SG-VERIFIER, CRYPTOGRAPHER, FORMAL-JUDGE live through
their floor successors; DESTROYER, MUTATOR, EXPERIMENTALIST, SYNTHESIZER
structure-only; **seat nine UNRESOLVED (NH-10) — never invented.**

## Carried to the site repo (all under swarm/)

`index.html` (the door + the floor) · `README.md` · `CHARTER.md` ·
`STATUS.md` · `PROOF.md` · `register/register.jsonl` ·
`register/REGISTER_STATE.json` · `seats/` (25 charters) ·
`workflows-to-push/` (2 reference copies).

## Excluded from the landing (named, by design)

- `scripts/` (`stand_up_floor.py`, `mirror_register.py`,
  `issues_manifest.json`) — the GitHub-issues floor's machinery; the site
  floor generates from the kit instead.
- `labels.json` — the GitHub label spec; no function on the site floor.
- `hookup/WORKING_COPY_HOOKUP.md` — its premise (create the-swarm) is
  superseded by this landing.
- `push/` — the repo-push manifest for the superseded plan.
- `.github/workflows/` — the App cannot push workflow files anywhere
  (Workflows permission, item T1). Reference copies ride under
  `workflows-to-push/`; no workflow is placed by this landing.

## Taylor acts remaining

1. Pull `snowphamtom.github.io` in Working Copy — the floor (`swarm/`) is
   on his phone. No new repo, no creation step.
2. Speak at the door (https://sequesteredyeti.art/swarm/) — seat zero.
