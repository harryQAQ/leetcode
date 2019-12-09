class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        flag, tmpPos = -1, 0
        for it in s:
            res[tmpPos] += it
            if tmpPos == 0 or tmpPos == numRows - 1: flag = -flag
            tmpPos += flag
        print("".join(res))
        return "".join(res)


x = Solution()
x.convert("PAYPALISHIRING", 3)