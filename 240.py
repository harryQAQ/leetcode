class Solution:
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        if not rows:
            return False
        cols = len(matrix[0])
        if cols == 0:
            return False
        
        #起点
        x = rows - 1
        y = 0

        while x >= 0 and y < cols:
            if matrix[x][y] > target:
                x -= 1
            elif matrix[x][y] < target:
                y += 1
            else:
                return True
        return False