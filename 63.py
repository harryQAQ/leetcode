from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        #多加一列0 是为了处理边界情况：只有一列的情况
        #最终结果取倒数第二个即可
        dp = [1] + [0]*(n)
        for i in range(0,m):
            for j in range(0,n):
                dp[j] = 0 if obstacleGrid[i][j] else dp[j]+dp[j-1]
        return dp[-2]