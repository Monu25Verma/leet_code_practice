from collections import Counter


class Solution:

    # counter
    def findTheDifference(s: str, t: str) -> str:
        return list(Counter(t) - Counter(s))[0]
        print(Counter(s))[0]

        # count
        for i in range(len(s)):
            if i.count(t) != i.count(s):
                return i


print(Solution.findTheDifference("abcd", "abcde"))