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

    def build_internal(s_int):
        numerator = 0
        f = 0
        for ii, si in enumerate(s_int):
            numerator += 3 ** (k - 1 - ii) * 2 ** f
            f += si
        numerator_factors = factorint(n=numerator)
        numerator_factors_string = " ".join([f"{kkk}   " * kk
                                             for kkk, kk in reversed(numerator_factors.items())])
        magenta(text=s_int, end="     ")
        yellow(text=f"Numerator\t{numerator}", end="     ")
        cyan(text=f"{numerator / denominator:.5f}", end="     ")
        yellow(text=f"{numerator_factors_string}", end="     ")
        print()
        return numerator

    for i in range(1, k):
        build_internal(s_int=s[i:]+s[:i])

    return build_internal(s_int=s)


def check_bounds(n, k):
    red(f"n\t{n}")
    red(f"k\t{k}")
    if n > 2 * k:
        cyan(text=f"Bound error:\tn exceeds 2k by {n - 2 * k}")
        return False
    if 2 ** n <= 3 ** k:
        cyan(text=f"Bound error:\tn too small - negative denominator {2 ** n - 3 ** k}")
        return False
    return True


def build_denominator(n, k):
    denominator = 2 ** n - 3 ** k
    denominator_factors = factorint(n=denominator)
    red(f"Denominator\t{denominator}\t{denominator_factors}")
    return denominator


def check(s):
    s = tuple(int(ss) for ss in s)
    red(s)
    n = sum(s)
    k = len(s)
    if not check_bounds(n=n, k=k):
        return
    denominator = build_denominator(n=n, k=k)
    numerator = build_numerator(s=s, denominator=denominator)
    green(f"Ratio\t{numerator / denominator}")
    green(f"Ratio\t{(Rational(numerator, denominator))}")
