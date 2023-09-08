from typing import List

class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        value = {}  # val : index

        for i, n in enumerate(nums):
            diff = target - n           #9-2 ->7
            if diff in value:           # 7 in val
                return [value[diff], i]
            value[n] = i
        return


print(Solution.twoSum([2,7,11,15], 9))

