num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
op = input("enter an operator: ")

if(op == '+'):
    sum = num1+num2
    print(f"addition : {sum}")

elif(op == '-'):
    sub = num1 - num2
    print(f"subtraction : {sub}")

elif(op == '*'):
    mul = num1*num2
    print(f"multiplication : {mul}")

else:
    div = num1/num2
    print(f"division : {div}")
