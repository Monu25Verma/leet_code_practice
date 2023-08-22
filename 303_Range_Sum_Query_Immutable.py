from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = []
        curr = 0
        for i in nums:
            curr += i  # cur = 0 + (-2) = -2
            self.sums.append(curr)  # [-2,-2,1, -4, -2, -5]

    def sumRange(self, left: int, right: int) -> int:
        if left > 0 and right > 0:
            return self.sums[right] - self.sums[left - 1]
        else:
            return self.sums[left or right]

        # Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


