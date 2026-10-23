# PROOF — register mirror verification (floor landing, 2026-10-23)

The floor's register mirror was copied from the house register at the
landing and verified twice: by the builder's own full chain walk, and again
on the copied bytes in the staging tree (a second, independent walk).

| Check | Result |
|---|---|
| Mirror bytes == the house register's bytes | **True** (byte-identical) |
| Mirror file SHA-256 | `04f45328729dfd1d52781d845afa86de9a84a7239dba0132f76777aa01a43e01` |
| House register SHA-256 (same read) | `04f45328729dfd1d52781d845afa86de9a84a7239dba0132f76777aa01a43e01` |
| Mirror chain walk (independent, on the copy) | **VERIFIED — 354 rows, no break, no hash mismatch** |
| Mirror tip | `ac4e928d896878c84fd300725ab9b584006ebeb1a370f97750093c766e9785ed` |
| Tip == `REGISTER_STATE.json` tip | **True** |
| File SHA == `REGISTER_STATE.json` SHA | **True** |
| House chain check at the build | ok — 354 rows, tip `ac4e928d896878c8` |

The register is live and grows by appends at the house. This mirror is the
verified state at the landing (2026-10-23T14:36:11Z); it is refreshed and re-verified
before every publication, and a chain that does not verify is never mirrored.
