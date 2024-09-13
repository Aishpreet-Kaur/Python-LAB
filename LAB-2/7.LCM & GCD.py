import math

def calculate_gcd(x, y):
    return math.gcd(x, y)

def calculate_lcm(x, y):
    return abs(x * y) // calculate_gcd(x, y)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

gcd = calculate_gcd(num1, num2)
lcm = calculate_lcm(num1, num2)

print(f"GCD of {num1} and {num2} is: {gcd}")
print(f"LCM of {num1} and {num2} is: {lcm}")
