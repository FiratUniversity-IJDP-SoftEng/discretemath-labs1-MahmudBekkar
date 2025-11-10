#Q1 Write a function that determines if a positive integer is prime.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(2))  
print(is_prime(7))   
print(is_prime(10)) 
print(is_prime(2))   
print(is_prime(66))   
print(is_prime(33))  
print(is_prime(20))   

