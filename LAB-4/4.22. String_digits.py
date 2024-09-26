def contains_only_digits(s):
    return s.isdigit()

user_input = input("Enter a string: ")

if contains_only_digits(user_input):
    print("The string contains only digits.")
else:
    print("The string contains non-digit characters.")
