from typing import List
from collections import defaultdict

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        learn_mp = defaultdict(lambda : 0)
        res = 0
        for s in chars:
            learn_mp[s] += 1
        for word in words:
            tmp_mp = defaultdict(lambda : 0)
            for c in word:
                tmp_mp[c] += 1
            flag = True
            for k, v in tmp_mp.items():
                if learn_mp[k] < v:
                    flag = False
                    break
            if flag:
                res += len(word)
        return res
            

x = Solution()
print(x.countCharacters(["cat","bt","hat","tree"],
"atach"))




