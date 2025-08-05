def fibonacci(n):
    if n < 0:
        return "Input should be a non-negative integer"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Print Fibonacci numbers from F(0) to F(10)
for i in range(11):
    print(f"F({i}) = {fibonacci(i)}")
