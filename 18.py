from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        if n < 4:
            return res
        nums.sort()
        for i in range(0, n - 3):
            #防止重复
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # min sum > tar 跳出
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            #max sum < tar 下一轮
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue
            for j in range(i + 1, n - 2):
                 # 防止重复
                if j - i > 1 and nums[j] == nums[j-1]:
                    continue
                # 同理
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                # 同理
                if nums[i] + nums[j] + nums[n-1] + nums[n-2] < target:
                    continue
                # 双指针
                left = j + 1
                right = n - 1

                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]: left += 1
                        while left < right and nums[right] == nums[right - 1]: right -= 1
                        left += 1
                        right -= 1
                    elif sum > target:
                        right -= 1
                    else:
                        left += 1    
        return res