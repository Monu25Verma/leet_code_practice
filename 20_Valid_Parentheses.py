class Solution:
    def isValid(s: str) -> bool:
        if len(s) < 2:
            return False
        l = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                l.append(s[i])
            elif s[i] == ")":
                if len(l) != 0 and l[len(l) - 1] == "(":
                    l.pop(len(l) - 1)
                else:
                    return False
            elif s[i] == "]":
                if len(l) != 0 and l[len(l) - 1] == "[":
                    l.pop(len(l) - 1)
                else:
                    return False
            elif s[i] == "}":
                if len(l) != 0 and l[len(l) - 1] == "{":
                    l.pop(len(l) - 1)
                else:
                    return False
        if len(l) == 0:
            return True
        else:
            return False

print(Solution.isValid("()[]{}"))