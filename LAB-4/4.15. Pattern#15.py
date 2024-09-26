def mirrored_pyramid(n):
    for i in range(1, n+1):
        print(" " * (n - i) * 2, end="")
        for j in range(1, i+1):
            print(j, end=" ")
        print()

mirrored_pyramid(5)
