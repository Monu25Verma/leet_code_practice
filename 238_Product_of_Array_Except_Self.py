from typing import List


class Solution:
    def productExceptSelf(nums: List[int]) -> List[int]:
        res = [1] * len(nums)  # [1,1,1,1]
        prefix = 1
        for i in range(len(nums)):  # i = 4,
            res[i] = prefix  # res[1] = 1 ,# res[2] = 1  , res[3] = 2, res[4]  = 6
            prefix *= nums[i]  # prefix = 1 * 1 = 1, 2, 6, 24
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):  # 3,-1,-1 -> 3,2,1,0
            res[i] *= postfix  # res[1] = 1 , res[2] = 4, res[2] = 12, res[1] = 24
            postfix *= nums[i]  # postfix = 1 * 4 = 4, 12 ,24, 24
        return res


print(Solution.productExceptSelf([1,2,3,4]))