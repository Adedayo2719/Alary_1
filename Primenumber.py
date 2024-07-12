def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False  # other even numbers are not prime
    
    # Check for factors from 3 upwards
    sqrt_n = int(n**0.5) + 1
    for i in range(3, sqrt_n, 2):  # check odd numbers only
        if n % i == 0:
            return False
    
    return True

# Example usage:
num = 17
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
