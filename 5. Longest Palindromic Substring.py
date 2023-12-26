
def longestPalindrome(s):
    def check_center(right, left):
        if s[left] == s[right]:
            print("yess")
        else:
            print("No")
    for i in range(len(s)):
        odd_palindrom = check_center(i, i)
        even_palindrom = check_center(i, i + 1)
longestPalindrome('babad')


