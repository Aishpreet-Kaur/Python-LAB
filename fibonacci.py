num = int(input("enter a number of series needed:"))
num1 = 0
num2 = 1
next_num = num2
count = 1
while count<=num:
    print(next_num,end=" ")
    count += 1
    num1,num2 = num2,next_num
    next_num = num1 + num2
    print()
