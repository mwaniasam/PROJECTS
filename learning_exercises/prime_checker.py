import math

def check_prime(number):
    if number < 2:
        raise ValueError("Enter a number >= 2")
    for num in range(2, int(math.sqrt(number)) + 1):
        if number % num == 0:
            print(f"{number} is not a prime number")
            return
    print(f"{number} is a prime number!")

n = int(input("Enter a number to check for primality:\n"))
check_prime(n)
