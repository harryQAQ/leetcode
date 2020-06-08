from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(len(board)):
            if 'R' in board[i]:
                x = i
                break

        y = board[x].index('R')
        row = ''.join(board[x]).replace('.', '')
        col = ''.join(i[y] for i in board).replace('.', '')
        return row.count('Rp') + row.count('pR') + col.count('Rp') + col.count('pR')

x = Solution()
print(x.numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]))