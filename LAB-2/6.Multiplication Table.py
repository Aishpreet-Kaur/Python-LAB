def multiplication_table(number):
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

num = int(input("Enter the number:"))
multiplication_table(num)
