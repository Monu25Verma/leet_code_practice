# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


def isBadVersion(mid):
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            
            if isBadVersion(mid) == False:
                print(isBadVersion(mid))
                low = mid + 1
            else:
                high = mid - 1

        return low


print(Solution.firstBadVersion(5, 4))









