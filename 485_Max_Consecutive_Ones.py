from typing import List


class Solution:
    def findMaxConsecutiveOnes(nums: List[int]) -> int:
        k = ''.join(map(str,nums))          #110111
        max_len = 0
        l = k.split('0')

        for i in l:
            if len(i) > max_len:
                max_len = len(i)
        return max_len


print(Solution.findMaxConsecutiveOnes([1,1,0,1,1,1]))