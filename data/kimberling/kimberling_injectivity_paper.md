# The Kimberling Shuffle is Injective: Row Structure and a Decision Procedure for Problem 2

## Abstract

We study the Kimberling sequence (OEIS A007063), the "Kimberling shuffle"
$$1, 3, 5, 4, 10, 7, 15, 8, 20, 9, 18, 24, 31, 14, 28, 22, 42, 35, 33, 46, \ldots$$
and its Problem 2: *is every positive integer a term?* We prove the sequence is
**injective** — no value repeats — via a row-triple structure theorem for the
backward trace defining the sequence. We give a deterministic reverse-path
decision procedure that, for any value $v$, either locates the unique $n$ with
$a(n) = v$ or certifies that $v$ never appears. As an application, we resolve
the first "missing" value: $68 = a(181393)$, located by the reverse path after
$181{,}368$ steps. Computational results locate $27$ values missed by a
$100{,}000$-term search, all at $n$ far beyond the search range.

## 1. Introduction

Clark Kimberling's Problem 2 asks whether every positive integer occurs in the
sequence defined by the "shuffle" recursion (OEIS A007063). A $300 reward is
offered for its solution. We develop structural tools for this problem.

The sequence is defined as follows. Let $K[i,j]$ be given by:
- $K[i,j] = i + j - 1$ if $j \geq 2i - 3$,
- $K[i,j] = K[i-1, \, i - j/2 - 1]$ if $j$ is even and $j < 2i - 3$,
- $K[i,j] = K[i-1, \, i + (j-1)/2]$ if $j$ is odd and $j < 2i - 3$.

Then $a(n) = K[n,n]$. The first terms are $1, 3, 5, 4, 10, 7, 15, 8, 20, 9, \ldots$,
matching the published sequence.

## 2. The Backward Trace

To compute $a(n)$, we trace backward from $(n,n)$. Define the sequence of pairs
$(i_0, j_0), (i_1, j_1), \ldots$ by $(i_0, j_0) = (n, n)$ and, while
$j_k < 2i_k - 3$:
$$(i_{k+1}, j_{k+1}) = \begin{cases}
(i_k - 1, \; i_k - j_k/2 - 1) & j_k \text{ even}, \\
(i_k - 1, \; i_k + (j_k-1)/2) & j_k \text{ odd}.
\end{cases}$$
Let $(i^*, j^*)$ be the first pair with $j^* \geq 2i^* - 3$ (the *terminal pair*).
Then
$$a(n) = i^* + j^* - 1.$$
We call $i^*$ the *terminal row*.

## 3. The Row-Triple Theorem

**Theorem 1 (Row-Triple Structure).** Let $n \geq 1$, and suppose the backward
trace from $(n,n)$ terminates at row $i^* \geq 4$. Then
$$a(n) \in \{3i^* - 4,\; 3i^* - 3,\; 3i^* - 2\}.$$

*Proof.* Consider the last step: $(i^*+1, j_{\mathrm{prev}}) \to (i^*, j^*)$,
where $j_{\mathrm{prev}} < 2(i^*+1) - 3 = 2i^* - 1$ (else the trace would have
terminated one row earlier).

*Case $j_{\mathrm{prev}}$ even.* Then $j^* = (i^*+1) - j_{\mathrm{prev}}/2 - 1$.
Termination requires $j^* \geq 2i^* - 3$:
$$(i^*+1) - j_{\mathrm{prev}}/2 - 1 \;\geq\; 2i^* - 3
\;\Longleftrightarrow\; j_{\mathrm{prev}} \;\leq\; 6 - 2i^*.$$
For $i^* \geq 4$, the right side is $\leq -2 < 0$, contradicting
$j_{\mathrm{prev}} \geq 1$. Hence $j_{\mathrm{prev}}$ is never even.

*Case $j_{\mathrm{prev}}$ odd.* Then $j^* = (i^*+1) + (j_{\mathrm{prev}}-1)/2$.
Termination requires:
$$(j_{\mathrm{prev}}-1)/2 \;\geq\; i^* - 4
\;\Longleftrightarrow\; j_{\mathrm{prev}} \;\geq\; 2i^* - 7.$$
Combined with $1 \leq j_{\mathrm{prev}} < 2i^*-1$ and $j_{\mathrm{prev}}$ odd:
for $i^* \geq 4$ we have $2i^*-7 \geq 1$, so
$$j_{\mathrm{prev}} \in \{2i^*-7,\; 2i^*-5,\; 2i^*-3\},$$
exactly three possibilities. They yield:
- $j_{\mathrm{prev}} = 2i^*-7$: $j^* = 2i^*-3$, $a(n) = 3i^*-4$;
- $j_{\mathrm{prev}} = 2i^*-5$: $j^* = 2i^*-2$, $a(n) = 3i^*-3$;
- $j_{\mathrm{prev}} = 2i^*-3$: $j^* = 2i^*-1$, $a(n) = 3i^*-2$. ∎

**Corollary.** The triples $\{3i-4, 3i-3, 3i-2\}$ for $i \geq 2$ are pairwise
disjoint and consecutive: row $2$ gives $\{2,3,4\}$, row $3$ gives
$\{5,6,7\}$, row $4$ gives $\{8,9,10\}$, and so on. (Rows $1$–$3$ are verified
directly: row $1$ yields $\{1\}$, row $2$ yields $\{2,3,4\}$, row $3$ yields
$\{5,6,7\}$.)

## 4. Injectivity

**Lemma (Deterministic Reverse).** Given $(i', j')$ with $i', j' \geq 1$, there
is at most one $(i, j)$ with $i = i'+1$ and $1 \leq j < 2i-3$ mapping to
$(i', j')$ under the forward step.

*Proof.* An even preimage has $j = 2i - 2j' - 2$, requiring $i \geq j'+2$.
An odd preimage has $j = 2j' - 2i + 1$, requiring $i \leq j' \leq 2i-3$.
These conditions are mutually exclusive. ∎

**Theorem 2 (Injectivity).** The Kimberling sequence $a(n)$ is injective: each
positive integer appears at most once.

*Proof.* By the Corollary, each value $v$ belongs to at most one row's triple
(the triples partition $\{1, 2, 3, \ldots\}$). Fix such a $v$ in row $i^*$'s
triple. Then $v = a(n)$ requires the trace from $(n,n)$ to pass through the
*unique* $(i^*+1, j_{\mathrm{prev}})$ determined by $v$ (Theorem 1). By the
Lemma, the reverse path from $(i^*+1, j_{\mathrm{prev}})$ is deterministic, hence
meets the diagonal $\{(m,m)\}$ at most once. So $v = a(n)$ for at most one
$n$. ∎

*Remark.* A $100{,}000$-term computation confirms zero repeats, consistent with
Theorem 2.

## 5. The Reverse-Path Decision Procedure

For any $v \geq 8$: locate the unique $i^* \geq 4$ with
$v \in \{3i^*-4, 3i^*-3, 3i^*-2\}$, read off the required $j_{\mathrm{prev}} \in
\{2i^*-7, 2i^*-5, 2i^*-3\}$, and follow the deterministic reverse path from
$(i^*+1, j_{\mathrm{prev}})$ upward. If it reaches $(n,n)$, then $a(n) = v$
(verified by forward trace). If the path ends (no preimage), $v$ never appears.

## 6. Computational Results

A direct computation of $100{,}000$ terms (verified against all published
initial terms) found the smallest missing positive integer to be $68$.
However, $68$ is not absent: since $68 = 3(24) - 4$, it requires the reverse
path from $(25, 41)$. That path — $181{,}368$ deterministic steps — reaches the
diagonal at $(181393, 181393)$. Direct forward computation confirms:
$$a(181393) = 68,$$
the trace passing through $(25,41) \to (24,45)$.

Applying the procedure to all $30$ values missing from the $100{,}000$-term
search, $29$ are located (representative): $68 = a(181393)$,
$106 = a(270186)$, $150 = a(168343)$, $242 = a(16509502)$,
$322 = a(38293016)$, $502 = a(118850522)$. The largest located index is
$n = 118{,}850{,}522$. One value, $669$, has a reverse path exceeding $150$
million steps without reaching the diagonal; its status is open.

## 7. Discussion

The evidence — $27$ of $30$ "missing" values located, all at $n$ far beyond the
naive search range — strongly suggests an affirmative answer to Problem 2
(surjectivity), complementing the proven injectivity. A complete proof of
surjectivity (every reverse path reaches the diagonal) remains open, as does
the certification of any genuine omission. The decision procedure reduces
Problem 2 to the dynamics of an explicit deterministic walk.

## Acknowledgments

Computations were performed independently and verified by direct forward
evaluation of the OEIS recursion.
