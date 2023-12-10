class Solution:
    def reverseWords(s: str) -> str:
        s = s.split()
        rev_word = [i[::-1] for i in s]
        return ' '.join(rev_word)

print(Solution.reverseWords("Let's take LeetCode contest"))