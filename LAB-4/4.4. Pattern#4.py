size = 5

for i in range(size, 0, -1):
    print(" " * (size - i), end="")
    print((str(i) + " ") * i)
