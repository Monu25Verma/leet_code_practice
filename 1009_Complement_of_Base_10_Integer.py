class Solution:
    def bitwiseComplement(n: int) -> int:  # n = 5
        com = ""
        for i in bin(n)[2:]:  # bin(5) -> 0b101 - > [2:]-> 101
            if i == "1":  # 1 == 1:
                com += "0"  # com = "" + '0' -> "0"
            else:
                com += '1'
        return int(com, 2)

print(Solution.bitwiseComplement(5))
