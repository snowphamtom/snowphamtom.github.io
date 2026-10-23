> **Landing note (2026-10-23, Taylor's directive 07:54 CT):** the floor lives on Taylor's site — sequesteredyeti.art/swarm/, inside snowphamtom/snowphamtom.github.io — superseding the private the-swarm repo plan named below (that repo was never created; the App is refused repo creation, 403 measured 2026-10-23). The charter below stands unchanged; read “this repo” as “this floor.” The GATE law is verbatim, as always. The workshop is the site, behind its door; GitHub’s copy of these files is the signpost and the mirror of record — it points to the workshop, it is not the workshop.

# THE FLOOR — CHARTER

**Repo:** `snowphamtom/the-swarm` (private — the floor's interior is confidential
and is not published).
**Design of record:** `Optimal_Bot_Swarm_Design_2026-10-22.html` (Monsters Ink LLC).
**Seats of record:** `seats.json` v1.1, adopted 2026-10-22.
**Spine:** the register — an append-only, hash-chained ledger. The house copy is
canonical; `register/register.jsonl` in this repo is its verified mirror.

## The admission law (the GATE) — Taylor's text, unchanged

> The swarm's admission law is the refusal law, unchanged: measure what is left over after an interaction; admit only what fits inside that leftover; otherwise refuse and record the refusal.
> A task is admitted to a seat only if it fits that seat's leftover — capacity, evidence, authority. Everything else is refused and the refusal is recorded.

## How the floor works on GitHub

- **One thread per seat.** Each seat has its own thread, which carries its
  charter: the seat's wing, occupant, cadence, capacity, and scopes from
  `seats.json`. No seat speaks outside its own thread.
- **Admission events** (a packet admitted, a packet refused, a receipt) are
  recorded as comments on the seat's thread **and** as rows in the register.
  The register is the record; the thread shows the seat's state and history.
- **Standing is stated in words.** Each seat's page and thread state its
  seat, its wing, and its standing — live, structure-only, admitted, refused,
  or unresolved. On GitHub the standing is also carried as a label, so the
  board can be filtered. A change of standing is recorded with its reason,
  in the same act.
- **The HIVE is a wing of this floor**, not a second repo — one floor, per
  the design of record. Its nine seats carry `wing:hive` + `hive:<name>`.
  Four live through their successors on the floor; four are structure-only;
  the ninth seat is **unresolved** — its name appears in no held record,
  and it is never invented.
- **TOLL's limits carry over exactly:** TOLL cannot sign, send, submit, or
  spend. Its scopes here are what they are at the house: sweep, adjudicate, stage.
- **Standing grants** (recorded in `seats.json`): GitHub write and Gmail,
  each to 2026-11-19, and an all-access grant dated 2026-10-22. A standing
  grant never covers disclosure: publishing unfiled matter needs Taylor's
  decision on the act itself.

## What is live, with and without the Actions workflows

The Muse GitHub App can read/write issues, comments, labels, and ordinary
files here — **the floor runs on those powers alone from its first push.**
The App cannot create this repo (403, measured 2026-10-23) and cannot push
workflow files (the Workflows permission is a change only Taylor can make;
  it has not been made).

- **Live without workflows:** every seat issue and its thread; label state;
  the register mirror as files (pushed by the mirror script under the
  house push lock); Taylor's own reading and hand, through the Working Copy
  app on his phone.
- **Added when Taylor pushes `.github/workflows/` from Working Copy:**
  `register-mirror-check` re-verifies the mirrored chain on a 30-minute
  rhythm and comments on the register issue if the chain ever breaks;
  `seat-heartbeat` posts a cycle-state comment on the FLOW seat issue hourly.
  Until then, the house machine's own scheduled jobs (the FLOW 30-minute
  sweep, the keeper watchdog) remain the rhythm, exactly as they are today.

## Durability — why this repo exists

The machine that runs the swarm is replaced by its platform roughly
hourly; the register and the keeper's log prove it. This repo is the durable
home of the record: the register mirror means the chain's verified state
survives any single machine's end and is readable from Taylor's phone. If
the house register and this mirror ever disagree, the mirror's
`REGISTER_STATE.json` names the last verified tip — the chain is re-derived
from the house original, never from the mirror alone.

*Staged 2026-10-23T12:45:31Z. Register at staging: 325 rows, tip `5e59f5b80db0ab1b`.*
