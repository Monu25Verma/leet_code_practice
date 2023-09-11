from typing import List


class Solution:
    def findMin(nums: List[int]) -> int:
        # print(min(nums))
        # return min(nums)

        low = 0  # 0
        high = len(nums) - 1  # 5-1 -> 4
        res = nums[0]  # 3

        while low <= high:  # 0 <= 4
            if nums[low] <= nums[high]:  # 3<= 1
                res = min(res, nums[low])
                break

            mid = (low + high) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid - 1
        return res

print(Solution.findMin([4,5,6,7,2,1,2]))