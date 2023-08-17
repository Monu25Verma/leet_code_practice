from typing import List


class Solution:
    def missingNumber(nums: List[int]) -> int:
        return ((len(nums) * (len(nums) + 1)) // 2) - sum(nums)


print(Solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
