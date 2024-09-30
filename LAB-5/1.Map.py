def triple(num):
    return num * 3

user_input = input("Enter numbers: ")
numbers = list(map(int, user_input.split()))
result= list(map(triple, numbers))
print("Tripled numbers:", result)
