class Solution:
    def isUgly(n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:   # 61%2 = 1
            n /= 2   #61/2 = 30.5  = false
        while n % 3 == 0:
            n /= 3
        while n % 5 == 0:
            n /= 5
        return n == 1


print(Solution.isUgly(61))

