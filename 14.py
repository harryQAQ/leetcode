class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        # if len(strs) == 0: return ""
        # minLen = 1 << 31
        # for it in strs:
        #     if len(it) < minLen:
        #         minLen = len(it)
        # res = ""
        # for i in range(minLen + 1):
        #     tmpstr = strs[0][:i]
        #     flag = False
        #     for it in strs:
        #         if it[:i] != tmpstr:
        #             flag = True
        #             break
        #     if not flag:
        #         res = tmpstr
        # return res
        s = ""
        y = list(zip(*strs))
        print(y)
        for i in zip(*strs):
            if len(set(i)) == 1:
                s += i[0]
            else:
                break
        return s


x = Solution()
print(x.longestCommonPrefix(['ste', 'st']))