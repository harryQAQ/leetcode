from typing import List
from collections import defaultdict

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        prime, time = [], []
        d = defaultdict(int)
        for i in deck:
            d[i] += 1

        time = [value for key, value in d.items()]
        N, size = min(time), len(deck)
        if N < 2:
            return False
        check = [True] * (N + 1)
        #素筛得到小于N的所有素数
        for i in range(2, N + 1):
            if check[i]:
                prime.append(i)
                j = 2
                while j * i <= N:
                    check[j * i] = False
                    j += 1
        for i in prime:
            flag = False
            if size % i == 0:
                flag = True
                for cnt in time:
                    if cnt % i:
                        flag = False
                        break
            if flag:
                return True
        
        return False



x = Solution()
print(x.hasGroupsSizeX([1,1,1,1,1,0,0,0]))
        

        