from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        #p指针用来记录不重复的元素应该到哪个位置
        p = 1
        #i指针用来遍历
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                nums[p] = nums[i]
                p += 1
        return p

x = Solution()
print(x.removeDuplicates([1, 1, 2]))