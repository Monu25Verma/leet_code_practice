from typing import List


class Solution:
    def reverseString(s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return s.reverse()


print(Solution.reverseString(["h", "e", "l", "l", "o"]))
