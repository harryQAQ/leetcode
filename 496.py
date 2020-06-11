from typing import List
from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1: return []
        res  = [-1] * len(nums1)
        stack = []
        tmp = [0] * len(nums2)
        mp = defaultdict(lambda : -1)
        for idx, num in enumerate(nums2):
            while stack and stack[-1][1] < num:
                idx1, _ = stack.pop() 
                tmp[idx1] = nums2[idx]
            stack.append([idx, num])
        for i in range(len(tmp)):
            if tmp[i]:
                mp[nums2[i]] = tmp[i]
        for i in range(len(res)):
            res[i] = mp[nums1[i]]
        return res


x = Solution()
print(x.nextGreaterElement([4,1,2],[1,3,4,2]))