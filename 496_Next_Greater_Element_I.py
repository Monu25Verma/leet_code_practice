from typing import List


class Solution:
    def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []  # []

        for i in nums1:
            count = 0  #
            for j in nums2:
                if i == j:
                    for k in range(nums2.index(j) + 1, len(nums2)):  # (3, 4) ->3
                        if nums2[k] > j:  # 2 > 4
                            count += 1
                            ans.append(nums2[k])
                            break
                    if count == 0:
                        ans.append(-1)
        return ans

        if len(ans) == len(nums1):
            return ans


print(Solution.nextGreaterElement([4,1,2], [1,3,4,2]))









