def sum_of_cubes(n):
    return sum([i**3 for i in range(1,n+1)])

print(sum_of_cubes(200))

# Efficient method
def sum_of_cubes(n):
    return (n**2 * ((n+1)**2))/4


print(sum_of_cubes(200))
