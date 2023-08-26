class Solution:
    def titleToNumber(columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            x = ord(char) - ord('A') + 1  # ord(char) = A = 65 -65 = 0
            result = result * 26 + x
        return result

print(Solution.titleToNumber("A"))


