num = int(input("enter an number: "))

for i in range(2,num):
    if(num%i == 0):
        print(num,"it is not prime number")
        break
    else:
        print("it is a prime number")
        break

else:
    print("it is not prime number")
