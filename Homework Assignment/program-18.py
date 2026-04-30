def factorial_digits(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    
    return list(map(int, str(fact)))

# Example
print(factorial_digits(10))