class Solution:
    def lengthOfLongestSubstring(s: str) -> int:

        maxlength = 0
        charset = set()
        left = 0

        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left += 1
            charset.add(s[right])
            maxlength = max(maxlength, right - left + 1)

        return maxlength

print(Solution.lengthOfLongestSubstring("abcabcbb"))