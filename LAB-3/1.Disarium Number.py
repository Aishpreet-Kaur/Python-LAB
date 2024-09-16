def is_disarium(num):
    num_str = str(num)
    length = len(num_str)
    
    sum_of_digits = sum(int(digit) ** (index + 1) for index, digit in enumerate(num_str))

    return sum_of_digits == num

num = int(input("Enter a number: "))

if is_disarium(num):
    print(f"{num} is a Disarium number.")
else:
    print(f"{num} is not a Disarium number.")
