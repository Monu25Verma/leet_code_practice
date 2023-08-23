from typing import List


class Solution:
    def countBits(n: int) -> List[int]:
        offset = 1
        dp  = [0] * (n+1)               # [0,0,0,0,0,0]
        for i in range(1, n+1):         #  1,2,3,4,5
            if offset * 2 == i:         # 1 *2 == i not possible
                offset = i
            dp[i] = 1 + dp[i-offset]    # 1 + 1-1 =1 -> dp[1] = 1
            #[0,1,1,2,1,0]
        return dp

print(Solution.countBits(2))