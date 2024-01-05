import operator
class Solution:
    def findLengthOfLCIS(nums: list[int]) -> int:
        dp = [1] * len(nums)  # [1,1,1,1,1]
        for i in range(1, len(nums)):  # (1, 5)
            if nums[i] > nums[i - 1]:  # 3 > 2
                dp[i] += dp[i - 1]  #
        return max(dp)


print(Solution.findLengthOfLCIS([1, 3, 5, 4, 7]))
