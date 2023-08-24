class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s1, s2 = Counter(ransomNote), Counter(magazine) #'aa' -> a :2, 'ab' ->a:1, b:1
        if s1 & s2 == s1:                             #2 &1 = false
            return True
        else:
            return False


print(Solution.canConstruct("a", "b"))