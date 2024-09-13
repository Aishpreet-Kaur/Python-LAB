sum=0  
num=int(input("Enter a number:"))  
temp=num  

while(num):  
    i=1  
    fact=1  
    remainder=num%10  
    
    while(i<=remainder):  
        fact=fact*i   
        i=i+1  
    sum=sum+fact  
    num=num//10  

if(sum==temp):  
    print("Number is a strong number")  
else:  
    print("Number is not a strong number")  
