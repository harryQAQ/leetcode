from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def dfs(index, size, tmp, visit, nums):
            if len(tmp) == size:
                self.res.append(tmp.copy())
                return
            visit[index] = True
            for i in range(len(nums)):
                if not visit[i]:
                    tmp.append(nums[i])
                    dfs(i, size, tmp, visit, nums)
                    visit[i] = False
                    tmp.pop()
            visit[index] = False
        n = len(nums)
        visit = [False] * len(nums)
        for i in range(len(nums)):
            dfs(i, n, [nums[i]], visit, nums)
        return self.res

x = Solution()
print(x.permute([1, 2, 3]))