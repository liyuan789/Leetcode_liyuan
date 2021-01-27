def myPow(x, n):
    if n == 0:
        return 1

    if n >= 1:
        half = myPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x

    if n <= -1:
        half_abs = myPow(x, abs(n) // 2)
        if abs(n) % 2 == 0:
            return 1/(half_abs * half_abs)
        else:
            return 1/(half_abs * half_abs * x)


print(myPow(2, 10))
print(myPow(0, 10))

print(myPow(-2, 10))
print(myPow(-2, 9))

print(myPow(2, -10))
print(myPow(2, -9))