def factorial_digits(n):

    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return [int(digit) for digit in str(fact)]
n1 = 5
print("Input:", n1)
print("Output:", factorial_digits(n1))

n2 = 10
print("\nInput:", n2)
print("Output:", factorial_digits(n2))

n3 = 1
print("\nInput:", n3)
print("Output:", factorial_digits(n3))
