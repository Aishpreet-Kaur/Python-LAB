number = int(input("enter a number: "))
sum=0
for i in range(1, number):
    if number % i == 0:
       sum = sum + i
if sum == number:
    print('The given number is perfect number')
else:
    print('The given number is not perfect number')
