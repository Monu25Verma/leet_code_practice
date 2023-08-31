class Solution:
    def arrangeCoins(n: int) -> int:
        res = 0
        l, r = 1, n  # 1, 8
        while l <= r:  # 1<=8 ->yess
            mid = (l + r) // 2  # mid = 9 //2 --> 4.5
            coins = (mid / 2) * (mid + 1)  # coins = 4/2 * 5 -> 2*5 -> 10
            if coins > n:  # 10> 8
                r = mid - 1  # r = 4-1 ->3
            else:
                l = mid + 1
                res = max(mid, res)
                #print(res)

        return res


print(Solution.arrangeCoins(8))





