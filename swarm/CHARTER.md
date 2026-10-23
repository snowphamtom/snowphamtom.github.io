> **Landing note (2026-10-23, Taylor's directive 07:54 CT):** the floor lives on Taylor's site — sequesteredyeti.art/swarm/, inside snowphamtom/snowphamtom.github.io — superseding the private the-swarm repo plan named below (that repo was never created; the App is refused repo creation, 403 measured 2026-10-23). The charter below stands unchanged; read “this repo” as “this floor.” The GATE law is verbatim, as always. The workshop is the site, behind its door; GitHub’s copy of these files is the signpost and the mirror of record — it points to the workshop, it is not the workshop.

# THE FLOOR — CHARTER

**Repo:** `snowphamtom/the-swarm` (PRIVATE — the swarm interior is confidential;
the impenetrable posture governs everything in this repo).
**Design of record:** `Optimal_Bot_Swarm_Design_2026-10-22.html` (Monsters Ink LLC).
**Seats of record:** `seats.json` v1.1, adopted 2026-10-22.
**Spine:** the register — an append-only, hash-chained ledger. The VM copy is
canonical; `register/register.jsonl` in this repo is its verified mirror.

## The admission law (the GATE) — Taylor's text, unchanged

> The swarm's admission law is the refusal law, unchanged: measure what is left over after an interaction; admit only what fits inside that leftover; otherwise refuse and record the refusal.
> A task is admitted to a seat only if it fits that seat's leftover — capacity, evidence, authority. Everything else is refused and the refusal is recorded.

## How the floor works on GitHub

- **One issue per seat.** A seat's issue is its thread and its charter: the
  body pins the seat's wing, occupant, cadence, capacity, and scopes from
  `seats.json`. No seat speaks without its issue.
- **Admission events** (a packet admitted, a packet refused, a receipt) are
  recorded as comments on the seat's issue **and** as rows in the register.
  The register is the proof; the issue is the window.
- **Labels are the state.** `seat:<id>` names the seat, `wing:<name>` its
  wing, `state:live|structure|admitted|refused|unresolved` its standing.
  A seat whose state label changes gets a comment saying why, in the same act.
- **The HIVE is a wing of this floor**, not a second repo — one floor, per
  the design of record. Its nine seats carry `wing:hive` + `hive:<name>`.
  Four live through their successors on the floor; four are structure-only;
  the ninth seat is **UNRESOLVED** (NH-10) and is never invented.
- **TOLL's limits carry over exactly:** TOLL cannot sign, send, submit, or
  spend. Its scopes here are what they are on the VM: sweep, adjudicate, stage.
- **Standing grants** (from `seats.json`): ALW-GITHUB-T2RZZ7 (github-write,
  to 2026-11-19), ALW-GMAIL-LCNRUX (gmail, to 2026-11-19),
  ALL-ACCESS-2026-10-22. Disclosure-class scopes are never covered by a
  standing grant: publishing unfiled matter needs Taylor's per-action decision.

## What is live, with and without the Actions workflows

The Muse GitHub App can read/write issues, comments, labels, and ordinary
files here — **the floor runs on those powers alone from its first push.**
The App cannot create this repo (403, measured 2026-10-23) and cannot push
workflow files (the Workflows permission is Taylor's item T1, ungranted).

- **Live without workflows:** every seat issue and its thread; label state;
  the register mirror as files (pushed by the VM mirror script under the
  house push lock); Taylor's window and hand through Working Copy.
- **Added when Taylor pushes `.github/workflows/` from Working Copy:**
  `register-mirror-check` re-verifies the mirrored chain on a 30-minute
  rhythm and comments on the register issue if the chain ever breaks;
  `seat-heartbeat` posts a cycle-state comment on the FLOW seat issue hourly.
  Until then, the VM's own crons (FLOW 30-minute sweep, the keeper watchdog)
  remain the rhythm, exactly as they are today.

## Durability — why this repo exists

The VM that runs the swarm dies to platform churn roughly hourly; the
register, the keeper, and the reaper record prove it. This repo is the durable
substrate: the register mirror means the chain's verified state survives any
single VM death and is readable from Taylor's phone. If the VM register and
this mirror ever disagree, the mirror's `REGISTER_STATE.json` names the last
verified tip — the chain is re-derived from the VM original, never from the
mirror alone.

*Staged 2026-10-23T12:45:31Z. Register at staging: 325 rows, tip `5e59f5b80db0ab1b`.*
