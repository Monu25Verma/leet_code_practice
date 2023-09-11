from typing import List


class Solution:
    def search(nums: List[int], target: int) -> int:
        low = 0  # [4,5,6,7,0,1,2]
        high = len(nums) - 1  # high = 6
        while low <= high:  # 4  <= 6
            mid = (low + high) // 2  # mid = 0+6//2 -> 3
            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:  # 4 <= 6
                if nums[low] <= target < nums[mid]:  # 4 <= 0 < 6
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1


print(Solution.search([4,5,6,7,0,1,2], 0))