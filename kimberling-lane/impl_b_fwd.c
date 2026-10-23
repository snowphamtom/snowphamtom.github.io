/* KIMBERLING CAMPAIGN — Implementation B (C).
 *
 * Independently derived from Implementation A: B works in the framework's
 * (i, d) coordinates (d = j - i) and obtains its reverse step by inverting
 * the FORWARD step of surjectivity_framework.md:
 *     s = d + i;  s even: d' = -s/2;   s odd: d' = (s+1)/2;   i' = i - 1.
 * Inverting at row i' (lower state) for the preimage at row i'+1:
 *     even step reversed (requires d' <= -1): d = -2 d' - i' - 1
 *     odd  step reversed (requires d' >=  1): d =  2 d' - i' - 2
 *     d' = 0 is the diagonal: a hit.
 * A preimage is valid only if its j = i + d lies in [1, 2i - 3).
 *
 * Forward trace (for independent verification of located values):
 * start (n, 0); while d < i - 3 apply the forward step; a(n) = 2i + d - 1.
 *
 * Modes:
 *   sweep LO HI        targets for i* in [LO, HI]; CSV: istar,v,hit,n
 *   locate V           reverse-construct value V; prints n or STUCK
 *   forward N          prints a(N) by the forward (i,d) trace
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef long long i64;

/* Reverse walk in (i, d). Starts at (I, d0). Returns 1 and sets *n_out if
 * the diagonal is reached, 0 if stuck (invalid preimage). */
static i64 STEP_CAP = 5000000000LL;  /* safety: report CAPPED, never hang */

static int rev_hit(i64 I, i64 d0, i64 *n_out, i64 *steps_out) {
    i64 i = I, d = d0, steps = 0;
    for (;;) {
        if (d == 0) { *n_out = i; *steps_out = steps; return 1; }
        if (steps >= STEP_CAP) { *steps_out = steps; return 2; }
        i64 dn;
        if (d <= -1) dn = -2 * d - i - 1;
        else         dn =  2 * d - i - 2;
        i64 inew = i + 1;
        i64 jnew = inew + dn;
        if (jnew < 1 || jnew >= 2 * inew - 3) { *steps_out = steps; return 0; }
        i = inew; d = dn; steps++;
    }
}

static i64 a_forward(i64 n) {
    i64 i = n, d = 0;
    while (d < i - 3) {
        i64 s = i + d;
        if ((s & 1LL) == 0) d = -s / 2;
        else                d = (s + 1) / 2;
        i--;
    }
    return 2 * i + d - 1;
}

int main(int argc, char **argv) {

    if (argc >= 2 && strcmp(argv[1], "deep") == 0) {
        i64 I = atoll(argv[2]), jprev = atoll(argv[3]);
        STEP_CAP = atoll(argv[4]);
        i64 n = -1, steps = 0;
        int hit = rev_hit(I, jprev - I, &n, &steps);
        printf("I=%lld jprev=%lld outcome=%s n=%lld steps=%lld cap=%lld\n",
               I, jprev, hit == 1 ? "HIT" : (hit == 0 ? "STUCK" : "CAPPED"),
               n, steps, STEP_CAP);
        return 0;
    }

    if (argc >= 2 && strcmp(argv[1], "fwdck") == 0) {
        /* fwdck N CKPTFILE [RESUME_I RESUME_D RESUME_STEPS]
         * Checkpointing forward (i,d) trace: a(N) with resume support. */
        i64 N = atoll(argv[2]);
        const char *ck = argv[3];
        i64 i = N, d = 0, steps = 0;
        if (argc >= 7) { i = atoll(argv[4]); d = atoll(argv[5]); steps = atoll(argv[6]); }
        i64 since_ck = 0;
        while (d < i - 3) {
            i64 s = i + d;
            if ((s & 1LL) == 0) d = -s / 2;
            else                d = (s + 1) / 2;
            i--; steps++;
            if (++since_ck >= 200000000LL) {
                since_ck = 0;
                FILE *f = fopen(ck, "w");
                if (f) { fprintf(f, "%lld %lld %lld\n", i, d, steps); fclose(f); }
            }
        }
        printf("a(%lld)=%lld steps=%lld\n", N, 2 * i + d - 1, steps);
        return 0;
    }
    if (argc >= 2 && strcmp(argv[1], "sweep") == 0) {
        i64 lo = atoll(argv[2]), hi = atoll(argv[3]);
        if (argc >= 5) STEP_CAP = atoll(argv[4]);
        printf("istar,v,hit,n,steps\n");
        for (i64 istar = lo; istar <= hi; istar++) {
            i64 I = istar + 1;
            i64 offs[3] = {7, 5, 3};
            for (int k = 0; k < 3; k++) {
                i64 v = 3 * istar - (offs[k] == 7 ? 4 : (offs[k] == 5 ? 3 : 2));
                i64 jprev = 2 * istar - offs[k];
                i64 n = -1, steps = 0;
                int hit = rev_hit(I, jprev - I, &n, &steps);
                printf("%lld,%lld,%d,%lld,%lld\n", istar, v, hit,
                       hit ? n : -1, steps);
            }
        }
        return 0;
    }
    if (argc >= 2 && strcmp(argv[1], "locate") == 0) {
        i64 v = atoll(argv[2]);
        /* v in {3i*-4, 3i*-3, 3i*-2}: i* = round((v+3)/3) adjusted */
        i64 istar = (v + 4) / 3;               /* ceil((v+2)/3); >= 4 for v >= 8 */
        i64 off;
        if (v == 3 * istar - 4) off = 7;
        else if (v == 3 * istar - 3) off = 5;
        else if (v == 3 * istar - 2) off = 3;
        else { printf("v=%lld not in any row triple\n", v); return 1; }
        i64 I = istar + 1, jprev = 2 * istar - off;
        i64 n = -1, steps = 0;
        int hit = rev_hit(I, jprev - I, &n, &steps);
        if (hit) printf("v=%lld istar=%lld n=%lld steps=%lld\n", v, istar, n, steps);
        else     printf("v=%lld istar=%lld STUCK steps=%lld\n", v, istar, steps);
        return 0;
    }
    if (argc >= 2 && strcmp(argv[1], "forward") == 0) {
        i64 n = atoll(argv[2]);
        printf("a(%lld)=%lld\n", n, a_forward(n));
        return 0;
    }
    fprintf(stderr, "usage: sweep LO HI | locate V | forward N\n");
    return 2;
}
/* deep mode appended: handled in main via early dispatch below */
