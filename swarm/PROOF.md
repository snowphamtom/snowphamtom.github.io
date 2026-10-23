# PROOF — register mirror verification (floor landing, 2026-10-23)

The floor's register mirror was copied from the VM canonical register at the
landing and verified twice: by the builder's own full chain walk, and again
on the copied bytes in the staging tree (a second, independent walk).

| Check | Result |
|---|---|
| Mirror bytes == VM original bytes | **True** (byte-identical) |
| Mirror file SHA-256 | `da75d5e4edba19605937ddccef48f2477a7e79ae540dde2a1770ed2ad14de62d` |
| VM original SHA-256 (same read) | `da75d5e4edba19605937ddccef48f2477a7e79ae540dde2a1770ed2ad14de62d` |
| Mirror chain walk (independent, on the copy) | **PASS — 329 rows, no break, no hash mismatch** |
| Mirror tip | `fa859918467cb28c4068168ae31291bcbbc915e51a997b8546f8838d5ac2a03c` |
| Tip == `REGISTER_STATE.json` tip | **True** |
| File SHA == `REGISTER_STATE.json` SHA | **True** |
| VM original via `register.py verify-chain` (at build) | ok — 329 rows, tip `fa859918467cb28c` |

The register is live and grows by appends on the VM. This mirror is the
verified state at the landing (2026-10-23T12:59:08Z); it is refreshed and re-verified
before every push, and a chain that does not verify is never mirrored.
