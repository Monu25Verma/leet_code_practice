class Solution:
    def convertToBase7(num: int) -> str:
        if num == 0:
            return 0
        a = ''
        if num < 0:
            num = - num
            a = '-'
        base7 = ''
        while num > 0:
            base7 = base7 + str(num % 7)
            num = num // 7
        return a + base7[::-1]


print(Solution.convertToBase7(-7))




