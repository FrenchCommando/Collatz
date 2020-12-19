from src import red, green, yellow, magenta, cyan


def hcount(a):
    return len(a) - a.count("0")  # base not 2 ?


def lcount(a):
    first_one = next((i for i, c in enumerate(a) if a[i] != "0"))
    last_one = next((i for i, c in enumerate(a[::-1]) if a[-i] != "0"))
    return len(a) - first_one - last_one + 1


def process(a, print_intermediate, base4):
    while a[-2] != "0" or a[-1] != "0":
        a += "0"
    s = list([int(c) for c in a])

    last_digit = 3 if base4 else 1

    def add(index):
        if (d := s[index]) != last_digit:
            s[index] = d + 1
        else:
            s[index] = 0
            add(index=index+1)

    def multiply(index):
        for _ in range(int(s[index]) * 2):  # multiply 3 means add 2
            add(index=index)

    # That's the x3 multiplication
    for i in range(len(s) - 1, -1, -1):
        multiply(index=i)

    if print_intermediate:
        green(text="".join(map(str, s)).replace("0", " "))

    # that's the +1
    first_one = next((i for i in range(len(s)) if s[i] != 0))

    def post_operation(index):
        # s[index] -= 1
        add(index=index)
    if s[first_one] == 2 and base4:  # missing 2 simplification means I add 2 instead of 1
        post_operation(index=first_one)
    post_operation(index=first_one)

    if base4:
        return "".join(map(str, s))
    return "".join(map(str, s[1:]))


def decompose(n, print_intermediate, print_forward,  stop_cross, base4=False):
    b = f"{n:b}"
    red(f"Input number {n}     Binary representation {b}")
    a = b[::-1]
    red(f"Regular binary {b}     Inverse binary {a}")
    if base4:
        def base2tobase4(s):
            if len(s) < 2:
                return s
            return str(int(s[0]) + 2 * int(s[1]))
        a = "".join([base2tobase4(s=a[i:i+2])for i in range(0, len(a), 2)])
        b = a[::-1]
        green(f"Base4 {b}     Inverse {a}")
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
        a = process(a, print_intermediate, base4)
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
