from typing import List

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        numLen = len(numbers)
        if not numLen: return 0
        left, right = 0, numLen - 1
        while left < right:
            mid = (left + right) >> 1

            if numbers[mid] > numbers[right]:
                left = mid + 1
            elif numbers[mid] < numbers[right]:
                right = mid
            else:
                right -= 1
        return numbers[left]

