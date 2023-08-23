class Solution:
    def reverseVowels(s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        rev = []
        for i in range(len(s)):
            if s[i] in vowels:
                rev.append(s[i])
        rev = rev[::-1]
        count = 0
        result = list(s)
        for i in range(len(result)):
            if result[i] in vowels:
                result[i] = rev[count]  # "" -> str  +
                count = count + 1
        return str("".join(result))


print(Solution.reverseVowels("leetcode"))



