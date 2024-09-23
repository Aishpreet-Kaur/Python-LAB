n = 5  # number of rows

for i in range(n, 0, -1):
    print(' ' * (n - i), end='')  # print spaces
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
