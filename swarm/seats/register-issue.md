# THE REGISTER — the spine

The register is an append-only, hash-chained ledger: every packet, admission,
refusal, receipt, and verdict is a row. The house copy is the original; this
floor carries its verified mirror at `register/register.jsonl` (one folder up
from these seats) with the digest state in `register/REGISTER_STATE.json`.

Mirror state at the floor's landing:

- **Rows:** 347
- **Tip:** `111a9d281cdfb352c65134cde1668747345ce8c623ad80b229b55abdc7330364`
- **Mirror file SHA-256:** `b9ba7e087df9f0f5029f80937f623fe6dbba9e14b1f3429087269b1780bf9b2b`
- **Chain verification:** VERIFIED against the mirror (byte-identical to the
  house original — see `PROOF.md` at the floor root)

The mirror is refreshed and re-verified before every publication; a chain
that does not verify is never mirrored. The register window on the floor's
door page carries this same state, as of the landing.
