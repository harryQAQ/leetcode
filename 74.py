from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        rows, cols = len(matrix), len(matrix[0])
        row, col = rows - 1, 0
        while row >= 0 and col < cols:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                col += 1
            else:
                row -= 1
        return False


x = Solution()
print(x.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3))
