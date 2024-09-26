def even_number_pyramid(n):
    for i in range(1, n+1):
        num = 10
        for j in range(i):
            print(num, end=" ")
            num -= 2
        print()

even_number_pyramid(5)
