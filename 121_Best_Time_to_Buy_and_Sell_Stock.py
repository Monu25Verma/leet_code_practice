from math import inf
from typing import List


class Solution:
    def maxProfit(prices: List[int]) -> int:
        minprice = float(inf)
        maxprofit = 0
        for i in range(len(prices)):  # 6
            if prices[i] < minprice:  # 7 < infinite-> yes
                minprice = prices[i]  # minprice = 7, 1

            elif prices[i] - minprice > maxprofit:  # 5 - 1 > 0 - > 4 > 0 -> yes
                maxprofit = prices[i] - minprice  # maxprofit = 4

        return maxprofit


print(Solution.maxProfit([7,1,5,3,6,4]))