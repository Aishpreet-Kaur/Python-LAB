def square_list(numbers):
    return list(map(lambda x: x ** 2, numbers))

numbers_input = input("Enter the numbers, separated by spaces: ")

numbers = list(map(int, numbers_input.split()))
squared_numbers = square_list(numbers)
print("The squared numbers are:", squared_numbers)
