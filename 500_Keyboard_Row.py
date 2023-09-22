from typing import List


class Solution:
    def findWords(words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        ans = []

        for i in words:
            y = i[0].lower()
            if y in row1:
                x = row1
            elif y in row2:
                x = row2
            else:
                x = row3
            for j in i.lower():
                if j not in x:
                    break
            else:
                ans.append(i)

        return ans

print(Solution.findWords(["Hello","Alaska","Dad","Peace"]))