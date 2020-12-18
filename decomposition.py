import argparse
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


def yellow(text, **kwargs):
    print(colored(text=text, color="yellow"), **kwargs)


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


def decompose(n, print_intermediate, print_forward,  stop_cross):
    b = f"{n:b}"
    red(f"Input number {n}     Binary representation {b}")
    a = b[::-1]
    red(f"Regular binary {b}     Inverse binary {a}")
    print()
    count = 0
    red(text=a.replace("0", " "), end=" " * 5)
    hc = hcount(a=a)
    magenta(text=f"     {hc}", end=" " * 5)
    lc = lcount(a=a)
    lc0 = lc
    cyan(text=f"     {lc}", end=" " * 5)
    print()
    history = [a]
    while hc != 1 and (lc >= lc0 or not stop_cross):
        a = process(a, print_intermediate)
        hc = hcount(a)
        lc = lcount(a=a)
        if print_forward:
            red(text=a.replace("0", " "), end=" " * 5)
            magenta(text=f"     {hc}", end=" " * 5)
            cyan(text=f"     {lc}", end=" " * 5)
            print()
        count += 1
        history.append(a)
    print(f"Count:\t{count} for\t{n}")
    for i, a in enumerate(history[::-1]):
        a_space = a.replace("0", " ")
        space_pad = " " * i
        green(text=f"{space_pad}{a_space}", end=" " * 5)
        hc = hcount(a)
        lc = lcount(a=a)
        magenta(text=f"     {hc}", end=" " * 5)
        cyan(text=f"     {lc}", end=" " * 5)
        print()

    for i, a in enumerate(history[::-1]):
        a_space = a.replace("0", " ")
        space_pad = " " * i * 0
        yellow(text=f"{space_pad}{a_space}", end=" " * 5)
        hc = hcount(a)
        lc = lcount(a=a)
        magenta(text=f"     {hc}", end=" " * 5)
        cyan(text=f"     {lc}", end=" " * 5)
        print()


if __name__ == '__main__':
    n_value = 837799
    print_intermediate_value = False
    stop_cross_value = False
    binary_input = False
    print_forward_value = False

    parser = argparse.ArgumentParser()
    parser.add_argument('-b', help='binary input', action="store_true")
    parser.add_argument('-c', help='show only high flight', action="store_true")
    parser.add_argument('-i', help='print intermediate values', action="store_true")
    parser.add_argument('-f', help='print forward values', action="store_true")
    parser.add_argument('number', help='starting number')
    args = parser.parse_args()

    if args.b:
        n_value = int(args.number, 2)
    else:
        n_value = int(args.number)

    if args.c:
        stop_cross_value = True
    if args.f:
        print_forward_value = True
        if args.i:
            print_intermediate_value = True

    decompose(
        n=n_value,
        print_intermediate=print_intermediate_value,
        print_forward=print_forward_value,
        stop_cross=stop_cross_value,
    )
