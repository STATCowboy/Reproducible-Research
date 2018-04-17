def fib(n=100):    # write Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

fibDef = fib()
fib50 = fib(50)

print(fibDef)
print(fib50)