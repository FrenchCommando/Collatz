import argparse
from src.cycle_check import check


n_value = '1010101010000111111'

parser = argparse.ArgumentParser()
parser.add_argument('number', help='starting number', default=n_value, nargs='?')
args = parser.parse_args()

n_value = args.number

check(s=n_value)
