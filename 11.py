from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height: return 0
        res, left, right= 0, 0, len(height) - 1 
        while left < right:
            res = max(res, (right - left)* min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res
