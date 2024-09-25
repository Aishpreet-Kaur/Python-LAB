number = 1
levels = 3
for i in range(1, levels + 1):
    for j in range(1, 2 * i):  
        if number < 10:  
            print(number, end=" ")
            number += 1
    print() 
