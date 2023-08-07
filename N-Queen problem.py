class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        post_dig = set()  # row + column
        neg_dig = set()  # row - column
        col = set()

        res = []
        board = [['.'] * n for i in range(n)]

        def backtracking(r):
            if r == n:  # condition if every queen is placed
                copy = [''.join(row) for row in board]
                res.append(copy)
                return  # return result

            for c in range(n):  # check at each and every position
                # check before placing the queen because here it is placed
                if c in col or (r + c) in post_dig or (r - c) in neg_dig:
                    continue

                col.add(c)
                post_dig.add(r + c)
                neg_dig.add(r - c)
                board[r][c] = "Q"

                backtracking(r + 1)

                col.remove(c)
                post_dig.remove(r + c)
                neg_dig.remove(r - c)
                board[r][c] = "."

        backtracking(0)
        return res




