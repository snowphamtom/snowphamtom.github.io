# THE REGISTER — the spine

The register is an append-only, hash-chained ledger: every packet, admission,
refusal, receipt, and verdict is a row. The VM copy is canonical; this floor
carries its verified mirror at `register/register.jsonl` (one folder up from
these seats) with the digest state in `register/REGISTER_STATE.json`.

Mirror state at the floor's landing:

- **Rows:** 329
- **Tip:** `fa859918467cb28c4068168ae31291bcbbc915e51a997b8546f8838d5ac2a03c`
- **Mirror file SHA-256:** `da75d5e4edba19605937ddccef48f2477a7e79ae540dde2a1770ed2ad14de62d`
- **Chain verification:** PASS against the mirror (byte-identical to the VM
  original — see `PROOF.md` at the floor root)

The mirror is refreshed and re-verified before every push; a chain that does
not verify is never mirrored. The register window on the floor's door page
carries this same state, recorded at the landing.

Labels: `floor:register`
