from typing import List


class Solution:
    def plusOne(digits: List[int]) -> List[int]:
        digits = digits[::-1]
        x = 1
        ans = []
        for i in range(len(digits)):
            ans = ans + [(digits[i]+x)%10]
            x = (digits[i]+x)//10
        if x:
            ans += [x]
        return ans[::-1]

        return digit[::-1]

print(Solution.plusOne([1,2,3]))