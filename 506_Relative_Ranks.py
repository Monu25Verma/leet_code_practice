from typing import List

import heapq
class Solution:
    def findRelativeRanks(score: List[int]) -> List[str]:
        # greater contain -> gold, silver, bronze,4,5
        max_heap = []
        for i, s in enumerate(score):
            heapq.heappush(max_heap, (-s, i))
            res = [0] * len(score)
            place = 1
        while max_heap:
            pos = heapq.heappop(max_heap)[1]
            if place > 3:
                rank = str(place)
            elif place == 1:
                rank = "Gold Medal"
            elif place == 2:
                rank = "Silver Medal"
            elif place == 3:
                rank = "Bronze Medal"

            res[pos] = rank
            place += 1

        return res



print(Solution.findRelativeRanks([5,4,3,2,1]))