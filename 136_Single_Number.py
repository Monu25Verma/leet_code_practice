from typing import List


class Solution:
    def singleNumber(nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = res ^ i
        return res



print(Solution.singleNumber([2,2,1]))
