def fib(n):
    if n <= 0: 
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)    # F(n) = F(n-1) + F(n-2)


print(fib(0))
print(fib(1))
print(fib(-2))
print(fib(5))
print(fib(10))
