import math

def generate_primes():
    number = 2
    while True:
        is_prime = True
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            yield number
        number += 1

prime_sequence = generate_primes()
for _ in range(10):
    print(next(prime_sequence))
