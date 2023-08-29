from typing import List


class Solution:
    def thirdMax(nums: List[int]) -> int:
        nums = list(set(nums))
        nums_= len(nums)
        if nums_ < 3:
           return max(nums)
        else:
            nums.sort(reverse=True)
            return nums[2]

print(Solution.thirdMax([3,2,1]))

