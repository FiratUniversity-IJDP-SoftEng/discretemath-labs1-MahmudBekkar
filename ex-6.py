def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_pseudoprime_base_2(n):
    if is_prime(n):
        return False  
    if pow(2, n-1, n) == 1:
        return True
    return False

print("Finding all pseudoprimes to base 2 up to 10000:")

pseudoprimes = []
for n in range(4, 10001): 
    if is_pseudoprime_base_2(n):
        pseudoprimes.append(n)

print(f"Found {len(pseudoprimes)} pseudoprimes to base 2:")
for p in pseudoprimes:
    print(p)
