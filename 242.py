class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = True
        a = set(s)
        b = set(t)
        
        if a == b:
            for i in a:
                res = res and s.count(i) == t.count(i)
        else:
            res = False
        return res    


x = Solution()
print(x.isAnagram("cat", "rat"))