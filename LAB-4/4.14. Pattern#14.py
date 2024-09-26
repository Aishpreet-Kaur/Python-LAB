def pyramid_of_alternate_numbers(n):
    num = 1
    for i in range(1, n+1):
        for j in range(i):
            print(num, end=" ")
        num += 2 
        print()

pyramid_of_alternate_numbers(5)
