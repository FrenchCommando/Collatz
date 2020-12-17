import sys
from termcolor import colored


def red(text, **kwargs):
    print(colored(text=text, color="red"), **kwargs)


def green(text, **kwargs):
    print(colored(text=text, color="green"), **kwargs)


def magenta(text, **kwargs):
    print(colored(text=text, color="magenta"), **kwargs)


def hcount(a):
    count = a.count("1")
    # green(text=count, end="\t")
    return count


def process(a):
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
    green(text="".join(s).replace("0", " "))

    # that's the +1
    first_one = next((i for i in range(len(s)) if s[i] == "1"))
    add(index=first_one)
    # magenta(text="".join(s).replace("0", " "))

    return "".join(s)


def decompose(n):
    b = f"{n:b}"
    red(f"Input number {n}\tBinary representation {b}")
    a = b[::-1]
    red(f"Regular binary {b}\tInverse binary {a}")
    count = 0
    red(text=a.replace("0", " "))
    while hcount(a) != 1:
        a = process(a)
        red(text=a.replace("0", " "))
        count += 1
    print()
    print(f"Count:\t{count} for\t{n}")


if __name__ == '__main__':
    if len(sys.argv) == 1:
        n_value = 1000000
    else:
        n_value = sys.argv[1]
    decompose(n=n_value)
