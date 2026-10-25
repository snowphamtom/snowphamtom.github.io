# PERSPECTIVE 12 — A SIGNATURE (built fully)

A value's signature is its trajectory: the reverse-walk path itself,
as a drawing. Two values never share a trajectory point (lanes are
disjoint — perspective 9, proved by in-degree ≤ 1 and checked on a
773,977-node graph with 0 shared nodes). So each value's trajectory
is a UNIQUE curve in (row, d) space — a fingerprint no other value
can produce.

## The signature (v = 502, the worked example)

- **The drawing:** 1,190 sampled states from the real reverse walk
  (traj_502.txt), plotted x = log10(row), y = d, gold polyline on
  black, blue start dot at (169, 164), gold arrival ring at
  (118850522, 0). File: KIMBERLING_SIGNATURE_2026-10-25.svg.
- **The fingerprint:** SHA-256 of the canonical sampled-trajectory
  bytes: 5353f24254d099eaecbdfcff59271da49b313de4fa745e2ed16eb0e374faf254.
  Dedupe by this hash (house law): same hash = same signature;
  different hash = different trajectory. No names involved.
- **The inversion (both ways, exact):** from the last state
  (118850522, 0), the forward trace gives a(118850522) = 502. From
  the first state (169, 164), the triple gives row 168, c = 5,
  v = 3×168 − 2 = 502. The signature recovers its value from
  either end — it is exact, not a projection (unlike perspective
  8's melody, which is quantized and lossy).

## Verification (recomputed for this build)

- Engine: `~/workspace/kimberling_video/signature.py` (fifth
  independent implementation of the walk rule).
- **Sampled states: 1,190, all distinct, row strictly increasing.**
  No repeats — the walk never revisits a state (perspective 4's
  no-loops, checked here on the samples).
- **End inversion: a(118850522) = 502. Start inversion:
  (169, 164) → 502.** Both exact.
- **Disjointness vs neighbors:** full trajectories computed here —
  v = 503: 1,519 states (1,518 steps); v = 504: 605 states
  (604 steps). Shared states with v = 502's sampled states: **0
  and 0.** The neighbors' curves pass nowhere through v = 502's
  sampled points — the fingerprint is exclusive, not just unique
  in name.
- **Drawing written:** KIMBERLING_SIGNATURE_2026-10-25.svg
  (15,026 B), house style (black #000000, gold #ffd94a, blue
  #57c8ff, mono type).

## The boundary (what "signature" does NOT mean)

- NOT the picture: the SVG is a RENDERING of the signature; the
  signature itself is the state list. A different rendering (the
  video's S2b panel, a different scale) shows the same signature;
  a different state list is a different signature, whatever it
  looks like.
- NOT the full walk: the sampled form (1,190 states) is a faithful
  SUBSET — every sampled state is a real walk state, none
  invented — but it is not the full 118,850,353-step signature.
  The full signature is not drawable point-by-point; the sampled
  form is the practical signature, and its hash is the fingerprint
  of the sampled form, not of the full walk. Conflating the two
  would overclaim the fingerprint's coverage.
- NOT a claim about other values: each value has its own
  signature; v = 502's signature proves nothing about v = 503's,
  and no signature proves anything about the 26 capped (their
  trajectories are unfinished — their signatures are partial,
  ending in flight, not at the diagonal).
- NOT an identity replacement: the signature and the identity
  (perspective 10) are two views of the same value — identity
  says WHERE it lives and WHAT proves it; signature shows the
  PATH. Either one recovers v; neither one replaces the other.

## What "fully" means for this perspective

The signature defined (trajectory as drawing + fingerprint) +
uniqueness grounded (disjoint lanes, proved + checked) and
demonstrated (0 shared states vs two neighbors' full trajectories)
+ invertibility verified both ways (end and start) + the drawing
written + the boundary stated (rendering vs signature, sampled vs
full, no cross-value claims). Statistics claimed only where
measured; uniqueness claimed only where proved or checked.
