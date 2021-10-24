# Lab 6 Q2

# Determine if number is a prime number

def prime(n, i):
    if n <= 2:
        return True
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return prime(n, i + 1)


print(prime(27, 2))
