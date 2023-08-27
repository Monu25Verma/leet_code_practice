class Solution:
    def isAnagram(s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        len_s = len(s_list)
        len_t = len(t_list)
        if len_s != len_t:
            return False
        s_list.sort()
        t_list.sort()

        for i in range(0, len_s):
            if s_list[i] != t_list[i]:
                return False
        return True


print(Solution.isAnagram("anagram","nagaram"))