class Solution:
    def addDigits(num: int) -> int:
        result = 0
        while num > 0:
            result += num % 10    #389 --> 9   # 8
            num  = num //10     #38  #3

            if result > 9 and num == 0:  #ifcondition greeter than single digit example 9 --> 11
                num = result
                result = 0
        return result
print(Solution.addDigits(67))