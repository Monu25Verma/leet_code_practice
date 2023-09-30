class Solution:
    def tribonacci(n: int) -> int:
        n1, n2, n3 = 0,1,1
        if n <= 2:
            return [0, 1,1][n]
            print([0, 1,1][n])

        for i in range(3, n+1):
            nth = n1 + n2 + n3
            n1 = n2
            n2 = n3
            n3 = nth
        return n3

print(Solution.tribonacci(2))