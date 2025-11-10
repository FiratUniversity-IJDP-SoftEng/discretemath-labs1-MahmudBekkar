#Q2 Write a function that lists all prime numbers less than or equal to a given positive integer.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def list_primes_up_to(n):
    primes = []
    for num in range(2, n + 1):  
        if is_prime(num):
            primes.append(num)
    return primes

print(list_primes_up_to(10))   # output [2, 3, 5, 7]
print(list_primes_up_to(20))   # output [2, 3, 5, 7, 11, 13, 17, 19]
print(list_primes_up_to(1))    # output []
