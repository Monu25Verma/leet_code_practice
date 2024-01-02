class Solution:
    def countBinarySubstrings(s: str) -> int:
        prev, curr = 0, 1
        output = 0
        N = len(s)
        for i in range(1, N):
            if s[i] != s[i - 1]:
                output += min(curr, prev)
                prev = curr
                curr = 1

            else:
                curr += 1
        return output + min(prev, curr)


print(Solution.countBinarySubstrings("00110011"))
