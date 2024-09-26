def connected_inverted_pyramid(n):
    for i in range(n):
        for j in range(n, i, -1):
            print(j, end=" ")
        for j in range(i+1, n):
            print(j+1, end=" ")
        print()

connected_inverted_pyramid(5)
