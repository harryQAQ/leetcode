from typing import List 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n - 2):
            #防止重复
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            #max sum < 0 下一轮
            if nums[i] + nums[n - 1] + nums[n - 2] < 0:
                continue
            left, right = i + 1, n - 1
            while left < right:
                tmp_sum = nums[i] + nums[left] + nums[right]
                if tmp_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]: left += 1
                    while left < right and nums[right] == nums[right - 1]: right -= 1
                    left += 1
                    right -= 1
                elif tmp_sum < 0:
                    left += 1
                else:
                    right -= 1
        return res

x = Solution()
print(x.threeSum([-1, 0, 1, 2, -1, -4]))

