# THE REGISTER — the spine

The register is an append-only, hash-chained ledger: every packet, admission,
refusal, receipt, and verdict is a row. The house copy is the original; this
floor carries its verified mirror at `register/register.jsonl` (one folder up
from these seats) with the digest state in `register/REGISTER_STATE.json`.

Mirror state at the floor's landing:

- **Rows:** 354
- **Tip:** `ac4e928d896878c84fd300725ab9b584006ebeb1a370f97750093c766e9785ed`
- **Mirror file SHA-256:** `04f45328729dfd1d52781d845afa86de9a84a7239dba0132f76777aa01a43e01`
- **Chain verification:** VERIFIED against the mirror (byte-identical to the
  house original — see `PROOF.md` at the floor root)

The mirror is refreshed and re-verified before every publication; a chain
that does not verify is never mirrored. The register window on the floor's
door page carries this same state, as of the landing.
