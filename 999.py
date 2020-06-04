from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(len(board)):
            if 'R' in board[i]:
                x = i
                y = board[i].index('R')
                break

        row = ''.join(board[x]).replace(',', '')
        col = ''.join(i[x] for i in board).replace(',', '')

        return row.count('Rp') + row.count('pR') + col.count('Rp') + row.count('pR')
