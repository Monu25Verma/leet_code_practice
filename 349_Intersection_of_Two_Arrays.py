from typing import List


class Solution:
    def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
        lst = []
        # for i in nums1:
        #     for j in nums2:
        nums = set(nums1) & set(nums2)
        return nums

#solution 2
        # values = [i for i in nums1 if i in nums2]
        # return set(values)


print(Solution.intersection([1,2,2,1],[2,2]))