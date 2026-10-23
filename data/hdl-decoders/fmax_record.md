# Measured Fmax — Both Decoders (2026-10-22, Taylor's PC)

Post-place-and-route, quoted from the final timing lines of the nextpnr
logs in `fmax/`:

- **decoder_f64: 21.98 MHz** — `fmax/v7_wrap_f64_pnr.log`
  ("Max frequency for clock '$glbnet$clk$TRELLIS_IO_IN': 21.98 MHz")
- **decoder_gf128: 23.24 MHz** — `fmax/v7_wrap_gf128_pnr.log`
  ("Max frequency for clock '$glbnet$clk$TRELLIS_IO_IN': 23.24 MHz")

The logs also carry the post-placement estimates (24.46 / 25.44 MHz);
the figures above are the post-route finals. The "(FAIL at 200.00 MHz)"
tag is the 200 MHz constraint target that was set; `--timing-allow-fail`
let routing complete so the achieved frequency is the reported one.

## Flow — exactly as run

- OSS CAD Suite build 20261022: Yosys 0.70+190, nextpnr-ecp5
  0.11.1-77-g6b438a1c (versions in `fmax/v7_versions.log`).
- Target: Lattice ECP5 **LFE5U-85F**, package CABGA381, no pin
  constraints (IOs auto-placed), `--seed 1 --freq 200
  --timing-allow-fail`.
- Both decoder tops are purely combinational, so each was measured in a
  registered wrapper — input register bank → the unmodified decoder →
  output register bank — the usage the RTL header itself prescribes
  ("register the I/O" for one classification per cycle). The decoder
  RTL was not modified. Critical paths run through
  `syndrome_calc.v`, as designed.
- Utilisation: decoder_f64 1,921 TRELLIS_COMB (2% of the device),
  decoder_gf128 1,987.

## The caveat, stated plainly

The netlists were produced with a shortened ABC LUT-mapping script
(`strash; if; mfs2; lutpack -S 1` — the mapping tail of the default
script). The stock full script's SAT-based front end did not finish on
this parity-heavy design (the ABC9 stage accumulated 1,093 CPU-seconds
without producing a netlist). These Fmax figures are real post-route
measurements **of those netlists** — a completed full-script run would
likely map somewhat better, so read these as measured floors for this
flow, not as the design's ceiling. Nothing here is derived from the
generic Yosys cell counts (5,055 / 5,236), and the swarm's circulating
"159,964 syndromes/sec / 6.25 µs" figure remains unmeasured and
unrelated to these numbers.
