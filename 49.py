from typing import List
from collections import defaultdict

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         lookup = defaultdict(list)
#         for s in strs:
#             lookup["".join(sorted(s))].append(s)
#         return list(lookup.values())



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
        print(len(prime))
        lookup = defaultdict(list)
        for _str in strs:
            key_val = 1
            for s in _str:
                key_val *= prime[ord(s) - 97]
            lookup[key_val].append(_str)
        return list(lookup.values())


x = Solution()
print(x.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
