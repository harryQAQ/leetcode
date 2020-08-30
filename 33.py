from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        n = len(nums)
        left, right = 0, n - 1
        while left < right:
            mid = left + (right - left + 1) // 2
            #右边是有序的
            if nums[mid] < nums[right]:
                #mid分在右边区间
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid - 1
            #左边有序
            else:
                #保证mid也在右边区间
                if nums[left] <= target <= nums[mid - 1]:
                    right = mid - 1
                else:
                    left = mid
        
        if nums[left] == target:
            return left
        return -1


