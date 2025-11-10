#Q3 Use a loop and the function above to determine whether 2^p - 1 is prime 
#   for each prime number p not exceeding 100.
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


for p in list_primes_up_to(100):
    mersenne = 2**p - 1
    if is_prime(mersenne):
        print(f"p = {p} → 2^{p} - 1 = {mersenne}  Prime ")
    else:
        print(f"p = {p} → 2^{p} - 1 = {mersenne}  Not Prime")

