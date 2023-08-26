class Solution:
    def hammingWeight(n: int) -> int:
        def bit(n, count):
            if n == 0:
                return count
            if n % 2 == 0:
                return bit(n // 2, count)
            else:
                return bit(n // 2, count + 1)

        return bit(n, 0)

print(Solution.hammingWeight(0o0000000000000000000000000001011))