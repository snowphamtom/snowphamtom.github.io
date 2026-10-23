# V4 Sidon — Verilog Decoders (both matrices)

Built and verified 2026-10-22. Two synthesizable repair-or-refuse decoders for
the 14×48 Sidon parity matrices, sharing one architecture:

- `syndrome_calc.v` — integer syndrome calculator: 48 signed lanes in
  (2'b01 = +1, 2'b00 = 0, 2'b11 = −1), 14 syndrome components out
  (3-bit two's complement each, packed [3r +: 3]).
- `sidon_classifier.v` — parallel-match classifier:
  syndrome = 0 → CLEAN (0); = ±column i → REPAIR (1, index i, sign);
  = ±axis row r → TAIL (2, index r, sign); anything else → REFUSE (3).
- `decoder_f64.v` — F₆₄ spec set (CONSOLIDATED DRAFT v3 §3.5 /
  construct_v4b.py MASKS4, F₂[t]/(t⁶+t+1), two common bits).
- `decoder_gf128.v` — GF(2⁷) fully-closed reserve-swapped set (seed6 with
  columns 8, 12, 16, 28, 36 swapped to reserve curve points; 69,184/69,184
  distinct triple syndromes).

Both tops are combinational; register the I/O and the block classifies one
syndrome per cycle.

## Verification (measured, this build)

Exhaustive RTL simulation (Icarus Verilog 11.0) against an independent Python
golden model (`gen_vectors.py`). Per decoder: 143,005 vectors — the zero
pattern, all 96 signed singles, all 28 signed tails, all 4,512 signed pairs,
all 138,368 signed triples (every sign assignment).

- decoder_f64:   142,977 patterns + 28 tails checked, 0 errors — PASS
- decoder_gf128: 142,977 patterns + 28 tails checked, 0 errors — PASS

Logs: `sim_f64.log`, `sim_gf128.log`. Vectors: `vectors/`.

## Synthesis (measured, this build)

Yosys 0.33, generic internal cell library (`proc; opt; techmap; opt`):

- decoder_f64:   classifier 1,515 cells + syndrome_calc 3,540 cells = 5,055
- decoder_gf128: classifier 1,586 cells + syndrome_calc 3,650 cells = 5,236

These are pre-mapping generic gate counts, not FPGA LUT counts and not ASIC
gate equivalents. No target library was used, so **no Fmax and no throughput
figure is claimed**. The "159,964 syndromes/sec / 6.25 μs" figure circulating
in swarm material remains unmeasured; a defensible number requires synthesis
against a named target library.

## Scope

All refusal guarantees are scoped to the verified fault model: equal-magnitude
(unit-amplitude) signed faults of weight ≤ 3 over the integers, plus the tail
(axis) lane. Unequal-amplitude behavior is covered only inside the bounded
window analyzed in the v3 draft (bot-reported [1/2, 5]); quadruples and above
are untested at RTL level.

## Status

Both matrices are NEW MATTER relative to the filed provisional 64/170,360
(which covers the 7-row [55,8] matrix only). This package is an engineering
artifact, not a filing document; any disclosure decision is Taylor's.

## Measured Fmax (2026-10-22, Taylor's PC)

The named-target requirement above was met. Post-place-and-route on a
Lattice ECP5 LFE5U-85F (nextpnr-ecp5, Yosys 0.70, seed 1, each decoder in
a registered-I/O wrapper, RTL unmodified): **decoder_f64 = 21.98 MHz;
decoder_gf128 = 23.24 MHz**. The netlists used a shortened ABC mapping
script (the full script's SAT front end did not finish on this design),
so these are measured floors for that flow, not the design's ceiling.
Full record: `fmax_record.md`; logs: `fmax/`. The same evening, both
decoders' exhaustive simulations also passed on the PC
(Icarus 14): 143,005 vectors each, 0 errors, TB RESULT: PASS.
