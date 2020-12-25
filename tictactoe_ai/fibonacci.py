def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(6))
