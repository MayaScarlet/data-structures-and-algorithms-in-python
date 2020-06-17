def is_multiple(n, m):
    if n%m == 0:
        return True
    return False

# Modified version
# def is_multiple(n, m):
#     if not isinstance(n and m, (int, float)):
#         print('No valid type')
#         return
#     if n%m == 0:
#         return True
#     return False

print(is_multiple(100, 10))
print(is_multiple(156, 9))
print(is_multiple(27, 8))
print(is_multiple(27, 'str'))
