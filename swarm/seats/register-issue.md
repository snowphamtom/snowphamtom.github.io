# THE REGISTER — the spine

The register is an append-only, hash-chained ledger: every packet, admission,
refusal, receipt, and verdict is a row. The house copy is the original; this
floor carries its verified mirror at `register/register.jsonl` (one folder up
from these seats) with the digest state in `register/REGISTER_STATE.json`.

Mirror state at the floor's landing:

- **Rows:** 334
- **Tip:** `0b18b01c3ae28ea5cc6bf15b3c3f4056886806e63bd4149d0f4e60f5c766ed43`
- **Mirror file SHA-256:** `879d5a931f5248229221d1409b646b0580c126d878ed6bcb5fd94bdb3cf820ed`
- **Chain verification:** VERIFIED against the mirror (byte-identical to the
  house original — see `PROOF.md` at the floor root)

The mirror is refreshed and re-verified before every publication; a chain
that does not verify is never mirrored. The register window on the floor's
door page carries this same state, as of the landing.
