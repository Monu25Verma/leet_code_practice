from typing import List


class Solution:
    def findDisappearedNumbers(nums: List[int]) -> List[int]:
        missing = []
        set_nums = set(nums)  # {1}
        for i in range(1, len(nums) + 1):  # 1, 2+1 -> 1,3 ->1,2
            if i not in set_nums:  # 2 not in set_nums
                missing.append(i)  # 2
        return missing  # 2

print(Solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]))

