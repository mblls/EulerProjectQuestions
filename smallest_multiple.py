# https://projecteuler.net/problem=5
# On paper answer: https://projecteuler.net/action=quote;post_id=393475

def smallest_number_divisible_by_n(n: int) -> int:
    for i in range(1, 1000000000):
        j = 0
        while j < n:
            j += 1
            if i % j != 0:
                break
        if j == n:
            return i
        i += n


print(smallest_number_divisible_by_n(20))

