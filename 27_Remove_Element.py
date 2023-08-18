from typing import List


class Solution:
    def removeElement(nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index


print(Solution.removeElement([3,2,2,3],3))