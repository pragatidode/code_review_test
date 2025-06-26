def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def is_even(n):
    if n<=1:
        return "Enter number greater than 1"
    if n % 2==0:
        return True
    return False

