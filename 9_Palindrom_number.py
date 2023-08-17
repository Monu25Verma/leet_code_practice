class Solution:
    def isPalindrome(x: int) -> bool:
        input_str = str(x)
        m = input_str[::-1]
        if input_str == m:
            return True
        else:
            return False


print(Solution.isPalindrome(121))