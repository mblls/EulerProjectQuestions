def smallest_number_divisible_by_n(n:int) -> int:
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
"""
Actual way to solve: https://projecteuler.net/action=quote;post_id=393475
1. Take every prime in the interval.
2. Take every prime to its largest power such that it is less than or equal to the max of the interval.
3. Take the product of these numbers to achieve the desired smallest number.
"""