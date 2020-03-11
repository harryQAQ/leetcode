from typing import List

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        #不是3的倍数一定不满足
        if s % 3 and s != 0:
            return False
        i, j = 0, len(A) - 1
        sumLeft, sumRight = A[i], A[j]
        while i + 1 < j:
            if sumLeft == sumRight == s / 3:
                return True
            if sumLeft != s / 3:
                i += 1
                sumLeft += A[i]
                
            if sumRight != s / 3:
                j -= 1
                sumRight += A[j]
                
        return False

x = Solution()
print(x.canThreePartsEqualSum([1,-1,1,-1]))