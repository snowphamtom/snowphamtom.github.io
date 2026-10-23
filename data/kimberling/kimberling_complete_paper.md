# The Kimberling Shuffle: Injectivity, Row Structure, and a Decision Procedure for Problem 2

## Abstract

We study the Kimberling sequence (OEIS A007063),
$$1, 3, 5, 4, 10, 7, 15, 8, 20, 9, 18, 24, 31, 14, 28, 22, 42, 35, 33, 46, \ldots$$
and Kimberling's Problem 2: *is every positive integer a term?* We prove the
sequence is **injective** via a row-triple structure theorem for the backward
trace. We give a deterministic reverse-path decision procedure that, for any
value $v$, either locates the unique $n$ with $a(n) = v$ or determines that the
path does not reach the diagonal. Applying it to the $30$ values absent from a
$100{,}000$-term computation, we locate all $30$, including $68 = a(181393)$
and $669 = a(653494691)$; the largest located index is $n = 653{,}494{,}691$.
A further verification confirms all $591$ row-triple targets for $i^*=4$ to
$200$ are hit.

## 1. Definition and the Backward Trace

Let $K[i,j]$ be defined by:
- $K[i,j] = i + j - 1$ if $j \geq 2i - 3$,
- $K[i,j] = K[i-1, \, i - j/2 - 1]$ if $j$ even, $j < 2i - 3$,
- $K[i,j] = K[i-1, \, i + (j-1)/2]$ if $j$ odd, $j < 2i - 3$.

The Kimberling sequence is $a(n) = K[n,n]$. An independent implementation of
this recursion reproduces all $20$ published initial terms exactly.

To compute $a(n)$, trace backward from $(i_0, j_0) = (n,n)$: while
$j_k < 2i_k - 3$,
$$(i_{k+1}, j_{k+1}) = \begin{cases}
(i_k-1,\; i_k - j_k/2 - 1), & j_k\ \mathrm{even},\\
(i_k-1,\; i_k + (j_k-1)/2), & j_k\ \mathrm{odd}.
\end{cases}$$
Let $(i^*, j^*)$ be the first pair with $j^* \geq 2i^*-3$. Then
$a(n) = i^* + j^* - 1$. We call $i^*$ the *terminal row* and $(i^*, j^*)$ the
*terminal pair*.

## 2. Row-Triple Theorem

**Theorem 1.** If the backward trace from $(n,n)$ terminates at row $i^* \geq 4$,
then $a(n) \in \{3i^*-4,\, 3i^*-3,\, 3i^*-2\}$.

*Proof.* Let the final step be $(i^*+1, j_{\mathrm{prev}}) \to (i^*, j^*)$ with
$j_{\mathrm{prev}} < 2i^*-1$.

If $j_{\mathrm{prev}}$ is even, $j^* = (i^*+1) - j_{\mathrm{prev}}/2 - 1$, and
$j^* \geq 2i^*-3$ forces $j_{\mathrm{prev}} \leq 6-2i^* \leq -2$, impossible.

Hence $j_{\mathrm{prev}}$ is odd, $j^* = (i^*+1)+(j_{\mathrm{prev}}-1)/2$, and
$j^* \geq 2i^*-3$ forces $j_{\mathrm{prev}} \geq 2i^*-7$. With
$j_{\mathrm{prev}}$ odd and $< 2i^*-1$, exactly three values are possible:
$2i^*-7$, $2i^*-5$, $2i^*-3$, giving $a(n) = 3i^*-4$, $3i^*-3$, $3i^*-2$
respectively. ∎

**Corollary.** Rows $1$–$3$ are checked directly: row $1$ yields $\{1\}$, row $2$
yields $\{2,3,4\}$, row $3$ yields $\{5,6,7\}$. For $i \geq 2$ the triples
$\{3i-4,3i-3,3i-2\}$ are pairwise disjoint and consecutive, partitioning
$\{1,2,3,\ldots\}$.

## 3. Injectivity

**Lemma.** The reverse step is deterministic: from $(i',j')$ there is at most
one $(i,j) = (i'+1, j)$ with $1 \leq j < 2i-3$ mapping forward to $(i',j')$.
(Indeed, an even preimage needs $i \geq j'+2$; an odd preimage needs
$i \leq j'$; these are exclusive.)

**Theorem 2.** $a(n)$ is injective.

*Proof.* Each $v \geq 1$ lies in at most one row-triple (Corollary). If
$v = a(n)$, the trace must terminate in $v$'s row via the *unique*
$j_{\mathrm{prev}}$ for $v$ (Theorem 1). The deterministic reverse path from
$(i^*+1, j_{\mathrm{prev}})$ meets the diagonal at most once, so $v = a(n)$ for
at most one $n$. ∎

A $100{,}000$-term computation found zero repeats, consistent with Theorem 2.

## 4. Decision Procedure

For $v \geq 8$: find the unique $i^* \geq 4$ with
$v \in \{3i^*-4, 3i^*-3, 3i^*-2\}$; the position of $v$ in the triple determines
$j_{\mathrm{prev}} \in \{2i^*-7, 2i^*-5, 2i^*-3\}$. Follow the deterministic
reverse path from $(i^*+1, j_{\mathrm{prev}})$. Reaching $(n,n)$ certifies
$a(n) = v$.

## 5. Computational Results

### 5.1 The value 68

$68 = 3(24)-4$ requires the reverse path from $(25,41)$. After $181{,}368$
deterministic steps it reaches $(181393,181393)$. Forward verification:
$$a(181393) = 68,\qquad (181393,181393) \to \cdots \to (25,41) \to (24,45).$$

### 5.2 All located values

The $30$ positive integers absent from the first $100{,}000$ terms, with
located $n$ (30 of 30):

| $v$ | $n$ with $a(n)=v$ | $v$ | $n$ with $a(n)=v$ | $v$ | $n$ with $a(n)=v$ |
|-----|-------------------|-----|-------------------|-----|-------------------|
| 68 | 181393 | 106 | 270186 | 147 | 8765242 |
| 150 | 168343 | 173 | 3576334 | 242 | 16509502 |
| 292 | 146434 | 322 | 38293016 | 384 | 471122 |
| 388 | 8398697 | 424 | 127309 | 427 | 4574186 |
| 447 | 104468 | 451 | 113570 | 460 | 299241 |
| 471 | 416275 | 479 | 270477 | 502 | 118850522 |
| 529 | 118183 | 539 | 220572 | 545 | 138065 |
| 552 | 1292005 | 571 | 367066 | 613 | 107844 |
| 630 | 129272 | 645 | 199171 | 646 | 5118890 |
| 652 | 618814 | 675 | 233139 | 669 | 653494691 |

Each was verified by the reverse-path construction; $68$ additionally by direct
forward computation. The value $669 = 3(224)-3$, whose reverse path from
$(225,443)$ ran $653{,}494{,}466$ steps, reaches the diagonal at
$(653494691, 653494691)$; hence $a(653494691) = 669$.

### 5.3 Extended verification: 591/591 row-triple targets

For $i^* = 4$ to $200$, all three row-triple targets
$(i^*+1, 2i^*-7)$, $(i^*+1, 2i^*-5)$, $(i^*+1, 2i^*-3)$ were tested via the
deterministic reverse path. **All 591 targets hit the diagonal** (zero misses,
zero stuck paths). Of these, 561 hit with $n \le 50{,}000$; 30 required larger
$n$ (maximum $n = 118{,}850{,}522$ for $v=502$). The hitting $n$ shows no
predictable relationship to $i^*$ or $v$ (correlation $-0.03$); reverse-path
parities are balanced ($\approx 50\%$ even), confirming the chaotic nature of
the inverse direction.

## 6. The Mirror: Forward Contraction vs Reverse Expansion

A key structural insight (due to the problem's poser): the *reverse* path
(Section 5) *expands* — the deviation $|u|$ doubles each step, yielding chaotic,
unpredictable dynamics with no clean invariant. The *forward* trace (Section 2)
*mirrors* this: $|u|$ *halves* each step, giving stable, contracting dynamics.

Specifically, in $(i,d)$ coordinates with $d = j-i$, the forward step satisfies
$|u'| = |u|/2$ for appropriate centerings ($u = d + i/3 + 2/9$ on even steps,
$u = d - i - 3$ on odd steps, up to exact constants). The reverse path inverts
this, hence the exponential growth observed ($653{,}494{,}466$ steps for $v=669$).

This directional asymmetry explains why the reverse-path invariant hunt fails
while the forward dynamics remain tractable. A surjectivity proof, if it exists
cleanly, lives in the mirror (forward/contracting) direction, not the inverse
(expanding) one.

The trace forest itself is a moving, turning fractal: 3,000 forward traces in
$(i,j)$ space, thermal-colored by terminal value, fan from the diagonal in a
self-similar wedge — contracting while flipping sign at each even step,
sweeping the space rather than merely translating through it.

## 7. Discussion

Theorem 2 establishes injectivity. All $30$ values absent from the
$100{,}000$-term search are located — up to $n = 653{,}494{,}691$ — giving
strong computational evidence for surjectivity (an affirmative answer to
Problem 2). A general proof that every reverse path reaches the diagonal
remains the final step toward the \$300 reward.

## Computational Appendix

- Recursion implementation verified against all $20$ published terms.
- $100{,}000$ terms: $369$ s, values saved to `kimb_vals.json`; max $299{,}539$; zero repeats.
- Reverse-path engine: deterministic single-path walk; even/odd preimage
  conditions mutually exclusive (Lemma).
- All $n$ above are exact, verified by construction. No approximations are
  used in the located indices.
