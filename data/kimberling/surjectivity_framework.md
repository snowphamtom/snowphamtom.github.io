# Surjectivity Proof Framework: The Mirror (Forward) Approach

## Setup

Forward trace in (i,d) coordinates, d=j-i:
- Start: (n, 0).
- If d+i even: (i,d) -> (i-1, -(d+i)/2).
- If d+i odd: (i,d) -> (i-1, (d+i+1)/2).
- Stop when d >= i-3. Value: a(n) = 2i* + d* - 1.

## Exact Contraction (The Mirror)

Define contracting coordinates:
- Even step (d+i even): u = d + i/3 + 2/9. Then u' = -u/2. (Contract + flip = TURNING.)
- Odd step (d+i odd): u = d - i - 3. Then u' = u/2. (Contract, no flip.)

Thus |u| halves each forward step (STABLE/MIRROR). Reverse doubles (UNSTABLE/INVERSE).

## Fixed Target Positions (Fractal Self-Similarity)

For value v in row i* (i*>=4), target is (I, j_t) where I=i*+1 and j_t in {2I-9, 2I-7, 2I-5}.

In (i,d): d_t = I - c where c in {9,7,5}. Then d+i = 2I-c (odd, since c odd).

Using odd centering: u_t = d_t - I - 3 = -c - 3.
- c=9: u = -12.
- c=7: u = -10.
- c=5: u = -8.

TARGETS ARE AT FIXED u POSITIONS, INDEPENDENT OF I. This is exact self-similarity.

## The Surjectivity Question

Prove: for each I>=5, the three targets (I, 2I-9), (I, 2I-7), (I, 2I-5) are hit by some forward trace from (n,n).

Computational: 591/591 hit for I=5..201 (i*=4..200). 561/591 with n<=50000.

## Open: Rigorous Bridge

From "targets at fixed u, reverse doubles |u|" to "reverse path must hit diagonal."

The u-coordinate gives exact self-similarity, but the parity-dependent centering switch complicates a direct proof.

Status: Framework complete, computational evidence strong, rigorous proof still open.
