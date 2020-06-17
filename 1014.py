from typing import List

class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        if not A: return 0
        #朴素的遍历会超时
        # res = -1
        # for l in range(0, len(A) - 1):
        #     if A[l] < A[l - 1] - 1:
        #         continue
        #     for r in range(l + 1, len(A)):
        #         if A[l] + A[r] + l - r > res:
        #             res = A[l] + A[r] + l - r
        res = -1
        pre_i_max = A[0] + 0
        for j in range(1, len(A)):
            res = max(res, pre_i_max + A[j] - j)
            pre_i_max = max(pre_i_max, A[j] + j)
        return res