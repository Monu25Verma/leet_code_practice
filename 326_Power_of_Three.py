class Solution:
    def isPowerOfThree(n: int) -> bool:
        if n > 1:
            while (n % 3 == 0):
                n //= 3
        return n == 1


print(Solution.isPowerOfThree(27))