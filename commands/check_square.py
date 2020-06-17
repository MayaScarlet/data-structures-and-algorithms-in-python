import argparse, math

"""
Checks if number is a perfect square and returns the square root.
If false, returns nearest perfect square
"""

parser = argparse.ArgumentParser(description='Checks if given number is a perfect square')
parser.add_argument('integer', type=int)


args = parser.parse_args()
value = int(args.integer)
sqrt = math.sqrt(value)
if (value % sqrt) == 0 :
    print (str(value) + ' is a perfect square of ' + str(int(sqrt)))
else:
    print(str(value) + ' is not a perfect square')
    nearest = math.ceil(sqrt) ** 2
    print('Nearest perfect square is ' + str(int(nearest)))
