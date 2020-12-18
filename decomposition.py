import argparse
from src.solver import decompose


n_value = 2 ** 6 - 1
print_intermediate_value = False
stop_cross_value = False
binary_input = False
print_forward_value = False

parser = argparse.ArgumentParser()
parser.add_argument('-b', help='binary input', action="store_true")
parser.add_argument('-c', help='show only high flight', action="store_true")
parser.add_argument('-i', help='print intermediate values', action="store_true")
parser.add_argument('-f', help='print forward values', action="store_true")
parser.add_argument('number', help='starting number', default=n_value, nargs='?')
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
