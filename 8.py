class Solution:
    def myAtoi(self, str: str) -> int:
        if not str: return 0
        str = str.lstrip()
        last = 0
        i = 2 if str[0] == '+' or str[0] == '-' else 1
        while i <= len(str):
            try:
                last = int(str[:i])
                i += 1
            except:
                break
        of = (1 << 31) - 1 if last >= 0 else -(1 << 31)
        if last> 0 and  last> of:
            last = of
        elif last < 0 and last < of:
            last = of
        return last
        


x = Solution()
print(x.myAtoi("+-2"))