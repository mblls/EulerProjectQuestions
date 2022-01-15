# https://projecteuler.net/problem=9

def is_pythagorean_triplet(a: int, b: int, c: int) -> bool:
    if a**2+b**2 == c**2:
        return True
    return False


def find_special_pythagorean_triplet(n: int) -> int:
    for a in range(1, n):
        for b in range(1, n):
            for c in range(1, n):
                if (a+b+c) == n and is_pythagorean_triplet(a, b, c):
                    return a*b*c
    return 0

print(find_special_pythagorean_triplet(1000))