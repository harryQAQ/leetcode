class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        hashMap = {}
        for id, it in enumerate(nums):
            hashMap[it] = id
        for id, it in enumerate(nums):
            another = hashMap.get(target - it)
            if another is not None and another != id:
                return[id, another]


x = Solution()
print(x.twoSum([3, 2, 4], 6))