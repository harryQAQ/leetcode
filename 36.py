from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        blocks = [ {} for _ in range(9)]
        for i in range(9):     #9个单位
            row = set(); col = set(); block = set()
            for j in range(9):  #每个单位9个数字
                if board[i][j] != '.': #行单位
                    if board[i][j] in row:
                        return False
                    else:
                        row.add(board[i][j])
                if board[j][i] != '.': #列单位
                    if board[j][i] in col:
                        return False
                    else:
                        col.add(board[j][i])
                now_box_id = (i // 3 ) * 3 + j // 3 
                if board[i][j] != '.': #添加进block单位
                    if blocks[now_box_id].get(board[i][j], -1) == -1: #block中不存在
                        blocks[now_box_id][board[i][j]] = 1
                    else:
                        return False
        return True