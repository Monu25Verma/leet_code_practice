from collections import Counter
from typing import List


class Solution:
    def commonChars(words: List[str]) -> List[str]:
        s = Counter(words[0])  # {c:1, o:2,l:1}
        for i in words:
            s = s & Counter(i)  #
        return list(s.elements())

print(Solution.commonChars(["cool","lock","cook"]))


