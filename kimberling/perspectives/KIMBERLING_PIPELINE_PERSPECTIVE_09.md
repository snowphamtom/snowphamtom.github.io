# PERSPECTIVE 9 — A PIPELINE (built fully)

The walk as a data pipeline. A lane is a value's reverse walk; a
stage is one reverse step; a lane's output is the diagonal (n, n).
The pipeline's shape is the theorem — and it is not the shape of a
typical pipeline.

## The shape (proved, then checked)

- **No merges.** Each state has at most one preimage
  (Deterministic-Reverse Lemma, PROVED — perspective 1).
  In-degree ≤ 1, always.
- **No forks.** From any state, exactly one of the two candidate
  preimages can be valid — both valid would give two preimages,
  contradicting the lemma. Out-degree ≤ 1, always. Out-degree 0 is
  exactly the STUCK (REFUSE) state, which never fired here.
- **No cycles.** i increases by exactly 1 at every step
  (perspective 4, PROVED). A lane never revisits a state.

So the pipeline is a **disjoint union of directed paths**:
independent lanes, no shared nodes, no junctions, no cycles. A
typical data pipeline merges streams and fans out; this one cannot.
Backpressure, fan-in, fan-out, and merge conflicts do not exist
here — the only flow question is how long a lane runs.

## The stages

Two stage types, from perspective 7's coin made into processing:
even-branch stages (contract-and-flip in the mirror variable) and
odd-branch stages (contract). Each stage halves the mirror magnitude
(perspective 5). A lane processes one state at a time, in order,
with no queue — the walk is sequential, so there is nothing to
buffer and nothing to schedule. Latency of a lane = its step count
(priced in perspective 11); throughput = one value per lane.

## Verification (recomputed for this build)

- Engine: `~/workspace/kimberling_video/pipeline.py` (third
  independent implementation of the walk rule, after gate.c/coin.c
  and music.py). Values v = 8..207, step cap 200,000 per lane.
- **Lanes: 200 values → ADMITTED 197, IN-FLIGHT 3, STUCK 0.**
  The 3 in-flight (v = 106, 147, 173) each hit the 200,000-step cap
  still ascending — in flight, not failed, not refused.
- **Graph: 773,977 nodes, 773,780 edges.** Nodes − edges = 197 =
  exactly the admitted lane count — the arithmetic of disjoint
  paths (each path has nodes = edges + 1), a second, structural
  confirmation of disjointness.
- **Violations: in-degree 0, out-degree 0, cycles 0, shared nodes 0.**
  Every node checked explicitly (predecessor map, successor map,
  i-increase assertion).
- **Stages: even 387,858, odd 385,922 (total 773,780).** Even share
  50.13% — the pipeline's stage mix matches the coin's ~50/50
  (perspective 7: 0.5000 over 205M steps).
- **Longest admitted lane: v = 68, 181,368 steps.** Mean admitted
  lane length: 3,927.8 steps.
- **Endpoint cross-check (independent direction):** for all 197
  admitted lanes, the forward trace from the endpoint (n, 0) back
  to the triple gives a(n) = v. **0 mismatches.** The lanes land
  on their own values' diagonal points, not just any diagonal point.
- **Large-scale evidence (cited, not re-run):** the C engines
  asserted ok1 ≠ ok2 at every step of all 205,349,937 steps across
  the 591 phase-1 walks (perspectives 1 and 7, 0 violations), and
  gate.c verified all 591 endpoints exactly (perspective 1). The
  bounded graph above is the explicit check; the C runs are the
  scale.

## The boundary (what "pipeline" does NOT mean)

- NOT a general DAG: no junctions exist to draw. Any diagram of
  this pipeline that shows streams merging or forking is wrong.
- NOT a claim about the swarm's data circuit: the swarm circuit
  (Gluttony → Rumplestiltskin → refiners → Wrath → Sloth → Pride)
  is Taylor's design with its own stages; the walk's lane shape is
  the same KIND of object (a lane, not a web), which is why the walk
  rule can serve as a data-circuit rule — stages in series, one
  input each, one output each. The analogy is structural, not a
  claim that either system proves anything about the other.
- NOT a performance claim: lane lengths vary from tens to
  181,368 steps in this bounded set (and to 4,733,476,427 in the
  full sweep) — a pipeline whose lanes differ by 5 orders of
  magnitude in latency has no meaningful "average throughput"
  without stating the distribution (perspective 6).

## What "fully" means for this perspective

The pipeline defined (lanes, stages, outputs) + its shape proved
(lemmas cited) and checked (773,977-node graph, 0 violations,
nodes − edges = lanes) + endpoints cross-checked in the forward
direction (0 mismatches) + stage census + the in-flight lanes
named, not hidden + the boundary stated. Statistics claimed only
where measured; the shape claimed only where proved or checked.
