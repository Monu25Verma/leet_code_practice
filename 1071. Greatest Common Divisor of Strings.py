str1 = "ABCABC"
str2 = "ABAB"

import math


class Solution:
    def gcdOfStrings(str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        gcdLen = math.gcd(len(str1), len(str2))
        return str1[:gcdLen]


print(Solution.gcdOfStrings("ABCABC", "ABAB"))
