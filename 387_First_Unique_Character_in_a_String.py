import collections
from collections import Counter


class Solution:
    def firstUniqChar(s: str) -> int:
        hset = collections.Counter(s)
        print(hset)
        for i in range(len(s)):
            if hset[s[i]] == 1:
                print(i)
        return -1

print(Solution.firstUniqChar("loveleetcode"))