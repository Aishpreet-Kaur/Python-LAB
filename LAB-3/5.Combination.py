def is_combination(n,r):
    return (fact(n) / (fact(r) * fact(n-r)))
    
def fact(n):
    i=1
    number=1
    while i<=n:
        number *= i
        i += 1
    return number
    
num=int(input("enter n:"))
res=int(input("enter r: "))
result= is_combination(num,res)
print(result)
