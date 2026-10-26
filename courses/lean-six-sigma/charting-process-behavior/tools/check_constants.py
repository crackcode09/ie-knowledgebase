"""Recompute d2 and d3 by numerical integration and compare with spc.py tables.

d2(n) = integral of [1 - (1-Phi(x))^n - Phi(x)^n] dx
E[R^2] via the joint distribution of min and max (double integral).

    python tools/check_constants.py
"""
import math
import os
import sys

import numpy as np
from scipy import integrate
from scipy.stats import norm

sys.path.insert(0, os.path.dirname(__file__))
import spc  # noqa: E402


def d2(n):
    f = lambda x: 1 - (1 - norm.cdf(x)) ** n - norm.cdf(x) ** n
    return integrate.quad(f, -12, 12)[0]


def d3(n):
    # E[R^2] = 2 * double integral over x<y of [1 - F(y)^n - (1-F(x))^n + (F(y)-F(x))^n] dx dy
    g = lambda x, y: 1 - norm.cdf(y) ** n - (1 - norm.cdf(x)) ** n + (norm.cdf(y) - norm.cdf(x)) ** n
    er2 = 2 * integrate.dblquad(lambda x, y: g(x, y), -9, 9, lambda y: -9, lambda y: y)[0]
    return math.sqrt(er2 - d2(n) ** 2)


ok = True
for n in range(2, 11):
    a, b = d2(n), d3(n)
    A2 = 3 / (a * math.sqrt(n))
    D4 = 1 + 3 * b / a
    D3 = max(0.0, 1 - 3 * b / a)
    row = [(spc.D2[n], a), (spc.D3_SD[n], b), (spc.A2[n], A2), (spc.D3[n], D3), (spc.D4[n], D4)]
    bad = [t for t, c in row if abs(t - c) > 0.0015]
    ok &= not bad
    print(f"n={n:2d} d2={a:.4f} d3={b:.4f} A2={A2:.4f} D3={D3:.4f} D4={D4:.4f} {'OK' if not bad else 'MISMATCH'}")
print("ALL OK" if ok else "CHECK TABLE")
