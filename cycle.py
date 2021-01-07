import argparse
from src.cycle_check import check


n_value = ['2', '1', '2', '2', '1', '1', '1', '4', '1', '2', '1', '2', '2', '1', '1', '5', '4', '1', '2', '1']

parser = argparse.ArgumentParser()
parser.add_argument('number', help='starting number', default=n_value, nargs='*')
args = parser.parse_args()

n_value = args.number

check(s=n_value)
