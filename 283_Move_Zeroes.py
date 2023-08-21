# from typing import List
#
#
# class Solution:
#     def moveZeroes(nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         i = 0
#         n = len(nums)
#         for j in range(n):
#             if nums[j] != 0:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 i += 1
#
#
#
# print(Solution.moveZeroes([0,1,0,3,12]))
#
class Solution:
    def wordPattern(pattern: str, s: str) -> bool:
        res = {}
        s = s.split()
        if len(pattern) != len(s):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in res.keys():
                if s[i] not in res.values():
                    res[pattern[i]] = s[i]
                else:
                    return False
            elif res[pattern[i]] != s[i]:
                return False
        return True

print(Solution.wordPattern("abba", "dog cat cat dog"))
        