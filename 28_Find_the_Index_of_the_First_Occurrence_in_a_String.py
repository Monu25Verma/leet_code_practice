class Solution:
    def strStr(haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0

        i = 0
        j = len(needle)
        while j <= len(haystack):
            currentneedle = haystack[i:j]
            if currentneedle == needle:
                return i
            i += 1
            j += 1
        return -1

print(Solution.strStr("sadbutsad","sad"))