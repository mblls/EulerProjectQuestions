# https://projecteuler.net/problem=7

def is_prime(num: int) -> bool:
    # We can speed up runtime by ignoring multiples of 2.
    if num % 2 == 0:
        return False
    # If a multiple is not found by searching all multiples
    # up to num//2+1, one won't exist in the second half either.
    for i in range(2, num//2+1):
        if num % i == 0:
            return False
    return True


def find_nth_prime(n: int) -> int:
    primes_found = 0
    num = 0
    while primes_found < n:
        num += 1
        if is_prime(num):
            primes_found += 1
    return num

print(find_nth_prime(6))