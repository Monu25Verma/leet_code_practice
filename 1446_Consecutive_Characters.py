class Solution:
    def maxPower(s: str) -> int:
        count, max_count = 1, 1
        prev = s[0]
        for i in range(1, len(s)):  # 0-7
            if s[i] == prev:  #
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1
                prev = s[i]
        return max_count

print(Solution.maxPower("leetcode"))
