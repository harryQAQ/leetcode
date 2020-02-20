from typing import List

class Solution:
    def countBits(self, num: int) -> List[int]:
        count = [0 for _ in range(num + 1)]
        for i in range(1, num + 1):
            count[i] = count[i & (i - 1)] + 1
        return count 

x = Solution()

print(x.countBits(2))