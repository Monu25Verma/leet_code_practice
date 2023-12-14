class Solution:
    def findLHS(nums: list[int]) -> int:
        map = {}
        count = 0
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = 1
            else:
                map[nums[i]] += 1
        if len(map) <= 1:
            return 0
        for key in map:
            if key + 1 in map:
                count = max(count, map[key] + map[key + 1])
        return count


print(Solution.findLHS([1, 3, 2, 2, 5, 2, 3, 7]))
