class Solution:
    def findComplement(num: int) -> int:
        com = ''
        while num > 0:  # 5 > 0
            if num % 2 == 1:  # 5 % 2 == 1 yes,
                com += '0'  # com = 0
            else:
                com  += '1'
            num = num // 2  # num = 5 // 2-> 2 , 2//2 = 1
        return int(com[::-1], 2)  #

print(Solution.findComplement(5))