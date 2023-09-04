# for prime number
def find_number(n):
    if n <= 1:
        return 0

    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1


def count_num(number):
    return bin(number).count('1')


class Solution:
    def countPrimeSetBits(left: int, right: int) -> int:
        ans = 0
        for number in range(left, right + 1):
            ans = ans + find_number(count_num(number))
        return ans

print(Solution.countPrimeSetBits(6, 10))