class Solution:
    def lengthOfLastWord(s: str) -> int:
        s = s.split()[::-1]
        return len(s[0])
print(Solution.lengthOfLastWord("Hello World"))
