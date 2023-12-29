import operator

nums = [1,3,5,4,7]
dp = [1] * len(nums)  # [1,1,1,1,1]
for i in range(1, len(nums)):  # (1, 5)
    if nums[i] > nums[i - 1]:  # 3 > 2
        dp[i] += dp[i - 1]  #
print(max(dp))

