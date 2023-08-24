from typing import List


class Solution:
    def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()  # [1,2,2,1]  --> [1,1,2,2]
        nums2.sort()  # [2,2]   ---> #[2,2]

        i = 0
        j = 0
        result = []
        while i < len(nums1) and j < len(nums2):  # 0<4   and  0<2
            if nums1[i] < nums2[j]:  # 1 <2
                i += 1  # 1
            elif nums2[j] < nums1[i]:  # 2< 1
                j += 1
            else:

                result.append(nums1[i])  # 2 == 2
                i += 1  # 2
                j += 1  # 2
        return result

print(Solution.intersect([1,2,2,1], [2,2]))

