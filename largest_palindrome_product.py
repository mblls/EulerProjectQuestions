# https://projecteuler.net/problem=4

def check_if_palindrome(num: int) -> bool:
    str_num = str(num)
    left, right = 0, len(str_num)-1
    while left <= right:
        if str_num[left] != str_num[right]:
            return False
        left += 1
        right -= 1
    return True


def find_palindrome_product() -> int:
    max_palindrome_product = float('-inf')
    max_palindrome_multiples = [0, 0]
    for num1 in range(100, 999):
        for num2 in range(100, 999):
            product = num1 * num2
            if check_if_palindrome(product) and product > max_palindrome_product:
                max_palindrome_product = product
                max_palindrome_multiples[0] = num1
                max_palindrome_multiples[1] = num2
    return max_palindrome_product


print(find_palindrome_product())