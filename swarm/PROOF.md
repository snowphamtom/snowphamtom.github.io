# PROOF — register mirror verification (floor landing, 2026-10-23)

The floor's register mirror was copied from the house register at the
landing and verified twice: by the builder's own full chain walk, and again
on the copied bytes in the staging tree (a second, independent walk).

| Check | Result |
|---|---|
| Mirror bytes == the house register's bytes | **True** (byte-identical) |
| Mirror file SHA-256 | `b9ba7e087df9f0f5029f80937f623fe6dbba9e14b1f3429087269b1780bf9b2b` |
| House register SHA-256 (same read) | `b9ba7e087df9f0f5029f80937f623fe6dbba9e14b1f3429087269b1780bf9b2b` |
| Mirror chain walk (independent, on the copy) | **VERIFIED — 347 rows, no break, no hash mismatch** |
| Mirror tip | `111a9d281cdfb352c65134cde1668747345ce8c623ad80b229b55abdc7330364` |
| Tip == `REGISTER_STATE.json` tip | **True** |
| File SHA == `REGISTER_STATE.json` SHA | **True** |
| House chain check at the build | ok — 347 rows, tip `111a9d281cdfb352` |

The register is live and grows by appends at the house. This mirror is the
verified state at the landing (2026-10-23T14:19:27Z); it is refreshed and re-verified
before every publication, and a chain that does not verify is never mirrored.
