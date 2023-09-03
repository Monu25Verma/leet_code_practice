class Solution:
    def hammingDistance(x: int, y: int) -> int:
        # z = x ^ y
        # count = 0
        # i = z
        # while i > 0:
        #     count += i % 2
        #     i = i //2
        # return count

        return bin(x ^ y).count('1')


print(Solution.hammingDistance( 1,  4))