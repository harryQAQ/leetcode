from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #确保nums1较短，这样查找起来快一些
        if len(nums1) > len(nums2):
            #交换他们的引用
            nums1, nums2 = nums2, nums1
        #上述交换保证了 m <= n，在更短的区间 [0, m] 中搜索，会更快一些
        m, n = len(nums1), len(nums2)

        # 使用二分查找算法在数组 nums1 中搜索一个索引 i
        left, right = 0, m
        # 因为 left_total 这个变量会一直用到，因此单独赋值，表示左边粉红色部分一共需要的元素个数
        # i + j == left_total
        left_total = (m + n + 1) >> 1

        while left < right:
            # 尝试要找的索引，在区间里完成二分，为了保证语义，这里就不定义成 mid 了
            i = (left + right) >> 1
            j = left_total - i

            #该条件一定不满足
            if nums2[j - 1] > nums1[i]:
                left = i + 1
            else:
                right = i

        # 退出循环的时候，交叉小于等于一定关系成立，那么中位数就可以从"边界线"两边的数得到
        i = left
        j = left_total - left

        # 边界值的特殊取法的原因在 PPT 第 10 张
        nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
        nums1_right_min = float('inf') if i == m else nums1[i]

        nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
        nums2_right_min = float('inf') if j == n else nums2[j]

        # 已经找到解了，分数组之和是奇数还是偶数得到不同的结果
        if (m + n) & 1:
            return max(nums1_left_max, nums2_left_max)
        else:
            return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2

        