class Solution:
    def repeatedSubstringPattern(s: str) -> bool:
        new_string = s * 2  # abc*2 - > abcabc
        new_string = new_string[1:-1]  # abcabc --> remove first and last value 1 and -1 ->bcab
        if s in new_string:  # abc in bca --> no
            return True
        else:
            return False  # return False


print(Solution.repeatedSubstringPattern("abab"))

