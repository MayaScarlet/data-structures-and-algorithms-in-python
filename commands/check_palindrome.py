import argparse

"""
Checks if given string is a palindrome or not
"""

parser = argparse.ArgumentParser(description="Checks if input string is palindrome")
parser.add_argument('string', type=str)

args = parser.parse_args()
input_string = args.string.lower()

# Check if input is a type str
inverse_string = input_string[::-1]
if input_string == inverse_string:
    print(str(input_string) + ' is a palindrome')
else:
    print('Not a palindrome')
