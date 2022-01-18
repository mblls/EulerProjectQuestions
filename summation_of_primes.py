# https://projecteuler.net/problem=10
from math import sqrt, floor


# Sieve of Eratosthenes O(n log log n)
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# The sieve of Eratosthenes allows us to find all primes
# in a range(n) in pseudo-polynomial time. It works by keeping
# track of all possible primes in a list as follows:
# 1. Start with 2 (first known prime)
# 2. Mark all multiples of 2 as False (not prime)
# 3. The next number marked True (in this case 3) will be
#    the next available prime. Repeat the process for all
#    values under sqrt(n).
def find_sum_of_primes_below_n(n: int) -> int:
    sum_of_primes = 0
    potential_primes = {x: True for x in range(n+1)}
    for i in range(2, floor(sqrt(n))):
        if potential_primes[i]:
            for j in range(i ** 2, n + 1, i):
                potential_primes[j] = False
    # 1 is not prime.
    potential_primes[1] = False
    for num, is_prime in potential_primes.items():
        if is_prime:
            sum_of_primes += num
    return sum_of_primes


print(find_sum_of_primes_below_n(2000000))