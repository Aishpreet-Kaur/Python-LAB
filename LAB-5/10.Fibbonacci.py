def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        next_fib = fib_seq[i - 1] + fib_seq[i - 2]
        fib_seq.append(next_fib)
    return fib_seq[:n] 
  
def square_fibonacci(n):
    fib_numbers = fibonacci(n)
    squared_fib_numbers = list(map(lambda x: x ** 2, fib_numbers))
    return squared_fib_numbers

N = int(input("Enter the number of Fibonacci numbers to compute: "))
result = square_fibonacci(N)
print(f"The squares of the first {N} Fibonacci numbers are: {result}")
