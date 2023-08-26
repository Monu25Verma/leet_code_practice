class Solution:
    def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
        indices = {}
        for ind, v in enumerate(nums):
            if (v in indices and ind - indices[v] <= k):
                return True
            indices[v] = ind
        return False

print(Solution.containsNearbyDuplicate([1,2,3,1],3))








