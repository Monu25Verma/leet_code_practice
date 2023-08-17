from typing import List

class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        value = {}  # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in value:
                return [value[diff], i]
            value[n] = i
        return


print(Solution.twoSum([2,7,11,15], 9))

