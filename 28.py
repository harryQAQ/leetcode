class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        if not needle: return 0
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                flag = True
                if i + len(needle) <= len(haystack):
                    for tmp_idx in range(i, i + len(needle)):
                        if haystack[tmp_idx] != needle[tmp_idx - i]:
                            flag = False
                            break
                else:
                    return -1
                if not flag: continue
                else: return i
        return -1

x = Solution()
print(x.strStr('a', 'a'))