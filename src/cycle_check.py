from src import red, green, yellow, magenta, cyan
from sympy.ntheory import factorint
from sympy.core import Rational


# check if the parity cycle identifier is an integer
# (100010100100010000)
# n is the number of slots
# k is the number of 1
# numerator: sum_{d=0}^(k-1) ( 3^d x 2^{a_{k-1-d}} )
#  a_i are the indices of the consecutive ones in the sequence
#  manipulating increments of a_i make shifting become cyclic permutation
# denominator: 2^n - 3^k

def build_numerator(s, denominator=1):
    k = len(s)
    numerator = 0
    f = 0
    for i, si in enumerate(s):
        numerator += 3 ** (k - 1 - i) * 2 ** f
        f += si
    # red(text=f"{numerator}")

    numerator_factors = factorint(n=numerator)
    numerator_factors_string = " ".join([f"{k}   " * kk for k, kk in reversed(numerator_factors.items())])
    if 2 not in numerator_factors:
        magenta(text=s, end="     ")
        yellow(text=f"Numerator\t{numerator}", end="     ")
        cyan(text=f"{numerator / denominator:.5f}", end="     ")
        yellow(text=f"{numerator_factors_string}", end="     ")
        print()
    return numerator


def check(s):
    s = tuple(int(ss) for ss in s)
    red(s)
    n = sum(s)
    k = len(s)
    red(f"n\t{n}")
    red(f"k\t{k}")

    denominator = 2 ** n - 3 ** k
    denominator_factors = factorint(n=denominator)
    red(f"Denominator\t{denominator}\t{denominator_factors}")

    for i in range(1, k):
        numerator = build_numerator(s=s[i:]+s[:i], denominator=denominator)
    numerator = build_numerator(s=s, denominator=denominator)

    green(f"Ratio\t{numerator / denominator}")
    green(f"Ratio\t{(Rational(numerator, denominator))}")
