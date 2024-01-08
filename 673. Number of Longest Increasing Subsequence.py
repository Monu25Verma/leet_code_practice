import operator
class Solution:
    def findLengthOfLCIS(nums: list[int]) -> int:
        dp = []
        for i in range(1, len(nums)):  # (1, 5)
            if nums[i] > nums[i - 1]:
                num = nums[i] - nums[i-1]
                dp.append(num)
            else:
                nums[i] += 1
        return max(dp)


print(Solution.findLengthOfLCIS([2,2,2,2,2]))
