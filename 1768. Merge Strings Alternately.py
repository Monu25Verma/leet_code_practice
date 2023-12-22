word1 = "abc"
word2 = "pqr"


class Solution:

    def mergeAlternately(word1: str, word2: str) -> str:
        result = []
        min_len = min(len(word1), len(word2))  # 3 3
        for i in range(min_len):
            result.append(word1[i])
            result.append(word2[i])

        result.extend([word1[min_len:], word2[min_len:]])
        return ''.join(result)


print(Solution.mergeAlternately('abc', 'pqr'))
