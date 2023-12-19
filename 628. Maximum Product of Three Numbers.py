class Solution:
    def maximumProduct(nums: list[int]) -> int:
        nums.sort(reverse=True)
        return max(nums[0] * nums[1] * nums[2], nums[0] * nums[-1] * nums[-2])


print(Solution.maximumProduct([1, 2, 3]))
