from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums : return []
        window, res = [], []    #window存放进入双端队列的下标
        for i, x in enumerate(nums):
            if i >= k and window[0] <= i - k:   #左侧下标超出队列大小时弹出左侧元素
                window.pop(0)
            while window and x >= nums[window[-1]]: #若新加入的大 就把其左边的一直弹出 ,保证最终是
                window.pop()
            window.append(i)
            if i >= k - 1:
                res.append(nums[window[0]])
        return res


x = Solution()
print(x.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))