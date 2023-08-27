class Solution:
    def isPowerOfTwo(n: int) -> bool:

        if n <= 0:
            return False

        if n == 1:
            return True

        while (n % 2 == 0):
            n /= 2

        return n == 1

print(Solution.isPowerOfTwo(1))