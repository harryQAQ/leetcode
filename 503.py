from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums: return []
        l = len(nums)
        res = [-1] * l
        stack = []
        for i in range( 2 * l - 1, -1, -1):
            while stack and stack[-1] <= nums[i % l]:
                stack.pop()
            res[i % l] = stack[-1] if stack else -1
            stack.append(nums[i % l])
        return res