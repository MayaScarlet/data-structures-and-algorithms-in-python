import argparse

"""
Returns sum of integers
"""

parser = argparse.ArgumentParser(
    description='Calculates sum of given integers'
)

parser.add_argument('integers', type=int, nargs="+")
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
