numbers = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
result = 1
for n in numbers:
    if n % 2 != 0:
        result *= n
print(result)
