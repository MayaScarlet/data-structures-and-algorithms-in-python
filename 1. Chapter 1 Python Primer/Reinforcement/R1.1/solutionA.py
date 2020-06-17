def is_even(k):
    if not isinstance(k, int):
        print('Input must be an integer')
        return
    return (k&1 == 0)

print(is_even(25))
print(is_even(20))
print(is_even('str'))

# Output:
# False
# True
# Input must be an integer
