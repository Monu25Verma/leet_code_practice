class Solution:
    def repeatedStringMatch(a: str, b: str) -> int:
        temp = a
        count = 1

        while len(a) < len(b) + 2 * len(temp):  # 4 < 9 + abcdabcd
            if b in a:
                return count
            a += temp
            count += 1
        return count

print(Solution.repeatedStringMatch("abcd","cdabcdab"))