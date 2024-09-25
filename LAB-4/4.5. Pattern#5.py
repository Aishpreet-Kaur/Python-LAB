digit = 5
levels = 5

for i in range(levels, 0, -1):
    print(" " * (levels - i), end="")
    print((str(digit) + " ") * i)
