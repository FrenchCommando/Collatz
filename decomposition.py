import sys
from colorama import init
from termcolor import colored

# use Colorama to make Termcolor work on Windows too
init()


def red(text, **kwargs):
    print(colored(text=text, color="red"), **kwargs)


def green(text, **kwargs):
    print(colored(text=text, color="green"), **kwargs)


def magenta(text, **kwargs):
    print(colored(text=text, color="magenta"), **kwargs)


def cyan(text, **kwargs):
    print(colored(text=text, color="cyan"), **kwargs)


def hcount(a):
    count = a.count("1")
    return count


def lcount(a):
    first_one = next((i for i, c in enumerate(a) if a[i] == "1"))
    last_one = next((i for i, c in enumerate(a[::-1]) if a[-i] == "1"))
    return len(a) - first_one - last_one + 1


def process(a, print_intermediate):
    while a[-2] != "0" or a[-1] != "0":
        a += "0"
    s = list(a)

    def add(index):
        if s[index] == "0":
            s[index] = "1"
        else:
            s[index] = "0"
            add(index=index+1)

    # That's the x3 multiplication
    for i in range(len(s) - 1, -1, -1):
        if s[i] == "1":
            add(index=i+1)
    if print_intermediate:
        green(text="".join(s).replace("0", " "))

    # that's the +1
    first_one = next((i for i in range(len(s)) if s[i] == "1"))
    add(index=first_one)

    return "".join(s[1:])


def decompose(n, print_intermediate, stop_cross):
    b = f"{n:b}"
    red(f"Input number {n}     Binary representation {b}")
    a = b[::-1]
    red(f"Regular binary {b}     Inverse binary {a}")
    count = 0
    red(text=a.replace("0", " "), end=" " * 5)
    hc = hcount(a=a)
    magenta(text=f"     {hc}", end=" " * 5)
    lc = lcount(a=a)
    lc0 = lc
    cyan(text=f"     {lc}", end=" " * 5)
    print()
    while hc != 1 and (lc >= lc0 or not stop_cross):
        a = process(a, print_intermediate)
        hc = hcount(a)
        lc = lcount(a=a)
        red(text=a.replace("0", " "), end=" " * 5)
        magenta(text=f"     {hc}", end=" " * 5)
        cyan(text=f"     {lc}", end=" " * 5)
        print()
        count += 1
    print(f"Count:\t{count} for\t{n}")


if __name__ == '__main__':
    n_value = 837799
    print_intermediate_value = False
    stop_cross_value = False
    if len(sys.argv) >= 2:
        n_value = int(sys.argv[-1])
    if len(sys.argv) >= 3:
        if sys.argv[-2] == "1":
            print_intermediate_value = True
    if len(sys.argv) >= 4:
        if sys.argv[-3] == "1":
            stop_cross_value = True

    decompose(
        n=n_value,
        print_intermediate=print_intermediate_value,
        stop_cross=stop_cross_value
    )
