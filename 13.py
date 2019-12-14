class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        res = 0
        last = 0
        for it in reversed(s):
            tmp = mapping[it]
            if tmp < last:
                tmp *= -1
            res += tmp
            last = abs(tmp)
        return res





x = Solution()
print(x.romanToInt("II"))