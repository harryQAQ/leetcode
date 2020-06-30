from typing import List 
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        size = len(nums)

        target = size - k
        left, right = 0, size - 1
        while True:
            index =  self.partition(nums, left, right)
            if index == target:
                return nums[index]
            elif index < target:
                left = index + 1
            else:
                right = index - 1
    # pivot设置为left
    #
    # def partition(self, nums, left, right):
    #     pivot = nums[left]
    #     j = left
    #     for i in range(left + 1, right + 1):
    #         if nums[i] < pivot:
    #             j += 1
    #             nums[i], nums[j] = nums[j], nums[i]
    #     nums[left], nums[j] = nums[j], nums[left]
    #     return j

    #povit随机选取
    def partition(self, nums, left, right):
        # 随机化切分元素
        # randint 是包括左右区间的
        # random_index = random.randint(left, right)
        # nums[random_index], nums[left] = nums[left], nums[random_index]
        random_index = random.randint(left, right)
        nums[random_index], nums[left] = nums[left], nums[random_index]

        pivot = nums[left]
        j = left
        for i in range(left + 1, right + 1):
            if nums[i] < pivot:
                j += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[left], nums[j] = nums[j], nums[left]
        return j

