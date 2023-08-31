from typing import List
class Solution:
    def findContentChildren(g: List[int], s: List[int]) -> int:
        greed = 0
        cookie = 0
        s.sort()
        g.sort()

        while greed < len(g) and cookie < len(s):   # 0< 3 and 0 < 2
            if s[cookie] >= g[greed]:
                # s[0] >= g[0]->=1>=1->1
                #[1] > g[1]->=1>2
                #not possible
                greed += 1                      # greedy = 2
            cookie +=1
        return greed                            #o/p - 2


print(Solution.findContentChildren([1,2],[1,2,3]))