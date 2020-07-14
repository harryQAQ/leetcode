from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        size = len(nums)

        hp = []
        for i in range(k):
            heapq.heappush(hp, nums[i])

        for i in range(k, size):
            top = hp[0]
            if nums[i] > top:
                heapq.heapreplace(hp, nums[i])
        
        return hp[0]
