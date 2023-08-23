class Solution:
    def isPalindrome(s: str) -> bool:
        s = [char.lower() for char in s if char.isalnum()]
        return s[::-1] == s


print(Solution.isPalindrome("A man, a plan, a canal: Panama"))
