from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #to save the rest numbers
        row = [set(range(1, 10)) for _ in range(9)]
        col = [set(range(1, 10)) for _ in range(9)]
        block = [set(range(1, 10)) for _ in range(9)]

        need_fill = []
        # get the rest numbers and pos that need to fill
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    now_val = int(board[i][j])
                    row[i].remove(now_val)
                    col[j].remove(now_val)
                    block[(i // 3) * 3 + j // 3].remove(now_val)
                else:
                    need_fill.append((i, j))

        def dfs(count):#count表示在need_fill中进行到第几个
            if count == len(need_fill):
                return True
            i, j = need_fill[count] #获取当前的位置
            box_id = (i // 3) * 3 + j // 3
            for tmp_num in row[i] & col[j] & block[box_id]: #填啥数字
                row[i].remove(tmp_num)
                col[j].remove(tmp_num)
                block[box_id].remove(tmp_num)
                board[i][j] = str(tmp_num)
                if dfs(count + 1):
                    return True
                row[i].add(tmp_num)
                col[j].add(tmp_num)
                block[box_id].add(tmp_num)
            return False #如果所有for循环都递归好了还没有return True 说明无解 
        dfs(0)


x = Solution()
print(x.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))