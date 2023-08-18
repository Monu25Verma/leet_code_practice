from typing import List


class Solution:
    def removeDuplicates(nums: List[int]) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]

        return j + 1


print(Solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))





