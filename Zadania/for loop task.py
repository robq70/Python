numbers = [-3, -2, -1, 0, 1, 2, 3]
set = {-1}
for n in numbers:
    if n % 2 != 0:
        set.add(n)
for n in set:
    print(n)

print("-----------------------------------")
