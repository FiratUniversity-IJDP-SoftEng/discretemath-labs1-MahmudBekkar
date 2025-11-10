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

print("Testing n^2 + n + 41 for n from 0 to 39:")
all_prime = True
for n in range(0, 40):
    value = n*n + n + 41
    if not is_prime(value):
        print(f"n = {n}: {value} is NOT prime!")
        all_prime = False

if all_prime:
    print("All values are prime for n from 0 to 39.")

n = 40
value = n*n + n + 41
print(f"\nTesting n = 40: {value}")
if is_prime(value):
    print("This is prime! (Unexpected)")
else:
    print("This is NOT prime as expected.")
