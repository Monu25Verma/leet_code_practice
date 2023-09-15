from typing import List


class Solution:
    def checkXMatrix(grid: List[List[int]]) -> bool:
        n = len(grid)  # n = 4
        for i in range(n):
            for j in range(n):
                if ((i != j and i + j != n - 1) and grid[i][j] != 0):  #
                    return 0
                elif ((i == j or i + j == n - 1) and grid[i][j] == 0):
                    return 0
        return 1

print(Solution.checkXMatrix([[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]))