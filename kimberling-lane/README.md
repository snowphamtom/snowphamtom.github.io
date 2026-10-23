# kimberling-verify — the Actions verification lane

Taylor Heller / Monsters Ink LLC. Built 2026-10-23 under the reach grant
(register: REACH entry) as redundancy for the local Kimberling fleet:
this lane's compute lives on GitHub's runners, so a local VM replacement
cannot kill it.

## What it does

`.github/workflows/kimberling-verify.yml` compiles `impl_b_fwd.c` and
reproduces, from scratch, the forward recomputation published in the
Kimberling data drop (`/data/kimberling/` on sequesteredyeti.art, README
§Verification):

- `fwdck 653494691` → `a(653494691)=669 steps=653494467`
- `forward` spot checks → a(181393)=68, a(168343)=150, a(471122)=384,
  a(4574186)=427, a(118850522)=502

Every run commits its record to `last-run.txt` in this folder (run id,
run URL, source SHA-256, verdict). A run that fails any check commits
nothing and shows red on the Actions page — silence here never means
success; the record file is the success.

## Basis

The recursion is published in the drop itself
(`kimberling_complete_paper.md`: K[i,j] and a(n) = K[n,n];
`surjectivity_framework.md`). `impl_b_fwd.c` is the campaign's
implementation of that published math, mirrored verbatim — its SHA-256
is printed in every run record. Before this lane was pushed, the line
`a(653494691)=669 steps=653494467` was reproduced locally twice: by the
campaign's compiled binary and by a fresh gcc -O2 compile of this source
(2026-10-23).

Scope note: this lane reproduces published results. Surjectivity of the
Kimberling sequence remains open; the claim packet stands NOT CLAIMABLE
and this lane changes nothing about that.
