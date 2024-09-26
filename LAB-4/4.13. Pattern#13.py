def pyramid_of_horizontal_tables(n):
    for i in range(n + 1):
        for j in range(i + 1):
            print(i * j, end=" ")
        print()

pyramid_of_horizontal_tables(6)
