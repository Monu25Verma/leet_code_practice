import math
class Solution:
    def checkPerfectNumber(num: int) -> bool:

        l = int(math.sqrt(num))  # 5
        print(l)
        sum = 0
        for i in range(1, l + 1):  # (1, 6)
            if num % i == 0:  # (28 % 1)->0
                sum += i  # sum = 0+1 ->1
                if i != num // i:  # 1 != 28 //i-> 28+ 0->28->1 != 28
                    sum += num // i  # sum = 1 + 28//i -> 1+0 ->1
        sum = sum - num  # sum = 1-
        return sum == num



print(Solution.checkPerfectNumber(28))