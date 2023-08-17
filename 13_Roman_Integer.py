class Solution:
    def romanToInt(s: str) -> int:

        # if first smaller that second then substact
        # if first bigger than add
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:  # 2< 3 and I < II
                res -= roman[s[i]]  # 0 - 1
            else:
                res += roman[s[i]]  # 0 + 1 = 1

        return res
print(Solution.romanToInt("III"))




