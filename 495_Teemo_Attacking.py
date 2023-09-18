from typing import List


class Solution:
    def findPoisonedDuration(timeSeries: List[int], duration: int) -> int:
        result = 0

        for i in range(len(timeSeries)-1):
            result += min((timeSeries[i+1]- timeSeries[i]),duration)
        return result + duration


print(Solution.findPoisonedDuration([1,2,3,4,5,6,7,8,9], 1))