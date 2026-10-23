# SEAT GATE — Admission

- **Wing:** ORCHESTRA
- **Occupant:** register.py gate + agent_gate.py + ALLOW-ONCE ledger
- **Placement:** vm
- **Cadence:** every packet
- **Status (seats.json):** LIVE
- **Capacity:** 99 open packets
- **Scopes:** `admit`, `refuse`

This issue is the seat's thread on the floor. Packets admitted to this seat,
refusals with their reasons, and receipts land here as comments — and as rows
in the register, which is the proof.

The admission law that governs this seat (Taylor's text, unchanged):

> measure what is left over after an interaction; admit only what fits inside that leftover; otherwise refuse and record the refusal A task is admitted to a seat only if it fits that seat's leftover — capacity, evidence, authority. Everything else is refused and the refusal is recorded.

Labels: `seat:gate` · `wing:orchestra` · `state:live`
