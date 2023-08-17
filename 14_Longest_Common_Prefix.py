class Solution:
    def longestCommonPrefix(strs: list[str]) -> str:
        longest_substring = strs[0]
        for i in range(1, len(strs)):
            j = 0
            new_substring = ""
            for k in strs[i]:
                print(k)
                if j < len(longest_substring) and k == longest_substring[j]:
                    #0< 6 and 1(f) == 0(f):
                    new_substring += k
                else:
                    break
                j += 1
                longest_substring = new_substring
            return longest_substring

print(Solution.longestCommonPrefix(["flower","flow","flight"]))