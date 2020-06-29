from typing import List

class Solution:
    # 原地哈希
    # 3 应该放在索引为 2 的地方
    # 4 应该放在索引为 3 的地方
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(size):
            #先要判断nums[i]是不是下标
            while 0 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
                self.__swap(nums, i, nums[i] - 1)
            
        for i in range(size):
            if nums[i] != i + 1:
                return i + 1

        return size + 1

    def __swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]