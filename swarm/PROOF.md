# PROOF — register mirror verification (floor landing, 2026-10-23)

The floor's register mirror was copied from the house register at the
landing and verified twice: by the builder's own full chain walk, and again
on the copied bytes in the staging tree (a second, independent walk).

| Check | Result |
|---|---|
| Mirror bytes == the house register's bytes | **True** (byte-identical) |
| Mirror file SHA-256 | `879d5a931f5248229221d1409b646b0580c126d878ed6bcb5fd94bdb3cf820ed` |
| House register SHA-256 (same read) | `879d5a931f5248229221d1409b646b0580c126d878ed6bcb5fd94bdb3cf820ed` |
| Mirror chain walk (independent, on the copy) | **VERIFIED — 334 rows, no break, no hash mismatch** |
| Mirror tip | `0b18b01c3ae28ea5cc6bf15b3c3f4056886806e63bd4149d0f4e60f5c766ed43` |
| Tip == `REGISTER_STATE.json` tip | **True** |
| File SHA == `REGISTER_STATE.json` SHA | **True** |
| House chain check at the build | ok — 334 rows, tip `0b18b01c3ae28ea5` |

The register is live and grows by appends at the house. This mirror is the
verified state at the landing (2026-10-23T13:20:44Z); it is refreshed and re-verified
before every publication, and a chain that does not verify is never mirrored.
