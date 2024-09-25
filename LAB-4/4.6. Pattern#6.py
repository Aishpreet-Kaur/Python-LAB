size = 5
for i in range(size, 0, -1):
    print(" " * (size - i), end="")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print() 
