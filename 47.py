def sum_cubes(n):
    total=0
    for i in range(1,n):
        total=total+(i**3)
    return total
print(sum_cubes(5))
