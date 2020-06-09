from typing import List

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        size = len(numbers)
        if size == 0:
            return 0

        left = 0
        right = size - 1

        while left < right:
            mid = (left + right) >> 1

            if numbers[mid] > numbers[right]:
                # 以[3, 4, 5, 1, 2]为例，当满足这个条件时，mid 以及 mid 的左边一定不是最小数字，mid和mid左边可以直接排除
                # 下一轮搜索区间是[mid + 1, right]
                left = mid + 1
            elif numbers[mid] == numbers[right]:
                # 只能把 right 排除掉，下一轮搜索区间是[left, right - 1]
                right = right - 1
            else:
                # 此时 numbers[mid] < numbers[right]
                # mid 的右边一定不是最小数字，mid 有可能是，下一轮搜索区间是[left, mid]
                right = mid
        return numbers[left]

