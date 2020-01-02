from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n < 3 or (not nums): return None
        nums.sort()
        gap = float('inf')
        for i in range(n):
            #剪枝
            if (i > 0 and nums[i] == nums[i - 1]): continue
            left, right = i + 1, n - 1
            while left < right:
                tempSum = nums[i] + nums[left] + nums[right]
                if abs(target - tempSum) < gap:
                    gap = abs(target - tempSum)
                    res = tempSum
                    if gap == 0: return target
                if tempSum - target < 0:
                    left += 1
                if tempSum - target > 0:
                    right -= 1
        print(res)
        return res

x = Solution()
x.threeSumClosest([1, 1, 1, 1], 0)