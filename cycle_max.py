from math import log, ceil

log8 = 3 * log(2)
log3b2 = log(3, 2)
print(f"log8\t{log8}")
print(f"log3 base2\t{log3b2}")


def n_from_k(k):
    return 1 / (log8 * diff_log(k=k))


def diff_log(k):
    n = ceil(k * log3b2)
    return n / k - log3b2


for u in range(-10, 10):
    kk = u + 190537
    print(f"k\t{kk}\t\t{diff_log(k=kk)}")


running_n = 0
k_index = 0  # 10781274
for kk in range(1, 114208327604):
    nn = n_from_k(k=kk)
    if nn > running_n:
        running_n = nn
        k_index = kk
    if kk % 1000000 == 0:
        print(f"k\t{kk}\t\tn\t{nn}\t\trunning n\t{running_n}\t\tk index\t{k_index}")
