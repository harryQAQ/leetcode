from typing import List
from collections import defaultdict

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        hashmap = defaultdict(int)
        for i in nums1:
            hashmap[i] += 1
        
        for i in nums2:
            if hashmap[i] > 0:
                res.append(i)
                hashmap[i] -= 1
        return res
