from sympy import nextprime
import random

print("Generating 10 different 100-digit prime numbers:")

primes = set()
while len(primes) < 10:
    start = random.randint(10**99, 10**100 - 1)
    p = nextprime(start)
    if len(str(p)) == 100:
        primes.add(p)

for i, prime in enumerate(sorted(primes), 1):
    print(f"{i}. {prime}")
