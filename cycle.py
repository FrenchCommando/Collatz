import argparse
from src.cycle_check import check


n_value = '10101010100001'

parser = argparse.ArgumentParser()
parser.add_argument('number', help='starting number', default=n_value, nargs='?')
args = parser.parse_args()

n_value = args.number

check(s=n_value)
