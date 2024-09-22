def sum_of_digits(number):
    return sum(int(digit) for digit in str(abs(number)))

number = int(input("Enter a number: "))
print(f"The sum of digits is: {sum_of_digits(number)}")
