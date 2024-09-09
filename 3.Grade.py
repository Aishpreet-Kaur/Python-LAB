percent = float(input("enter your marks: "))

if(percent >= 90):
    print("A")

elif((percent>=80) or (percent<=89)):
    print("B")
    
elif((percent>=70) or (percent<=79)):
    print("C")
    
elif((percent>=60) or (percent<=69)):
    print("D")
    
else:
    print("Fail")
