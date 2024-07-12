def factorial_iterative(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


# For Example:
num = 5
print(f"The factorial of {num} (using iterative approach) is: {factorial_iterative(num)}")
