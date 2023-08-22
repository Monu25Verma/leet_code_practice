
# Nim game means you have to do is eg: n = 4, it requires two players you have to pick the stone in such
# a way that n is not greater than the n so n = 4 the multiple of table 4 will give you value false
# it odes not satisify the condn
class Solution:
    def canWinNim(n: int) -> bool:
        if (n % 4) == 0:
            return False
        else:
            return True

print(Solution.canWinNim(4))