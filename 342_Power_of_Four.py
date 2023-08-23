class Solution:
    def isPowerOfFour(n: int) -> bool:
        return n in [4 ** i for i in range(0, 16)]

print(Solution.isPowerOfFour(16))