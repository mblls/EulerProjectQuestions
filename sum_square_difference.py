# https://projecteuler.net/problem=6
# on paper answer: https://projecteuler.net/action=quote;post_id=394062

def sum_of_squares(n:int) -> int:
    sum_of_n_squares = sum([i**2 for i in range(1, n+1)])
    return sum_of_n_squares


def square_of_sums(n:int) -> int:
    sum_of_n = sum([i for i in range(1, n+1)])
    return sum_of_n ** 2


print(square_of_sums(100)-sum_of_squares(100))