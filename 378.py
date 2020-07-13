from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix: return -1
        m, n = len(matrix), len(matrix[0])
        left, right = matrix[0][0], matrix[m - 1][n - 1]
        while left < right:
            mid = (left + right) >> 1
            index = self.findMidNums(matrix, mid)
            if index < k:
                left = mid + 1
            else:
                right = mid
        return left

    def findMidNums(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        count = 0
        for row in range(0, m):
            if matrix[row][n - 1] < target:
                count += n
                continue
            else:
                #找到当前行第一个大于target的数,结束的时候left/right即是当前行第一个大于target的下标
                left, right = 0, n
                while left < right:
                    mid = (left + right) >> 1
                    if matrix[row][mid] > target:
                        right = mid
                    else:
                        left = mid + 1
                count += left
        return count