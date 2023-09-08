from typing import List


class Solution:
    def maxSubArray(nums: List[int]) -> int:
        current_sum = nums[0]   #-2
        max_sum = current_sum
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])        #max(1, -2+1) - >(1,-1) max-1
            max_sum = max(max_sum, current_sum)
        return max_sum


print(Solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))