#!/usr/bin/env python3
"""Numerical spot-verification of RH: first 25 zeros, on-line vs off-line.
EVIDENCE LABEL: computed (floating point, mpmath 50 dps) - verification, NOT proof."""
import mpmath as mp
mp.mp.dps = 50
zeros = []
max_resid = mp.mpf("0")
for n in range(1, 26):
    z = mp.zetazero(n)              # n-th zero on the critical line (Hardy Z machinery)
    t = mp.im(z)
    val = abs(mp.zeta(mp.mpc("0.5", t)))
    max_resid = max(max_resid, val)
    zeros.append((n, mp.nstr(t, 12), mp.nstr(val, 3)))
# off-line probes at the same heights: s = 0.6 + it and 0.4 + it must NOT vanish
off = []
for n in (1, 5, 10, 25):
    t = mp.im(mp.zetazero(n))
    off.append((n, mp.nstr(abs(mp.zeta(mp.mpc("0.6", t))), 4),
                   mp.nstr(abs(mp.zeta(mp.mpc("0.4", t))), 4)))
# zero counting vs Riemann-von Mangoldt main term at T=100
T = mp.mpf(100)
N_actual = 0
n = 1
while mp.im(mp.zetazero(n)) <= T:
    N_actual += 1; n += 1
N_approx = T/(2*mp.pi) * mp.log(T/(2*mp.pi)) - T/(2*mp.pi) + mp.mpf(7)/8
print(f"zeros 1..25 on s=1/2+it: max |zeta| residual = {mp.nstr(max_resid, 3)}")
for r in zeros[:3] + zeros[-2:]:
    print(f"  zero {r[0]:>2}: t = {r[1]:>16}  |zeta| = {r[2]}")
print("off-line probes (n, |zeta(0.6+it)|, |zeta(0.4+it)|):", off)
print(f"N(100): counted {N_actual} zeros with t<=100; Riemann-von Mangoldt main term = {mp.nstr(N_approx, 6)}")
