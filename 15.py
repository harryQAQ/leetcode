class Solution:
    def threeSum(self, nums: list) -> list:
        nums.sort()
        res = []
        for k in range(len(nums)):
            if nums[k] > 0: break
            if k > 0 and nums[k] == nums[k - 1]: continue
            i, j = k + 1, len(nums) - 1
            while i < j:
                if nums[k] + nums[i] + nums[j] < 0:
                    i += 1
                elif nums[k] + nums[i] + nums[j] > 0:
                    j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
        return res

x = Solution()
print(x.threeSum([-1, 0, 1, 2, -1, -4]))

