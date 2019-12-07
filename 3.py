class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        #指针记录滑窗左边界, 右边界就是idx
        left, maxlen = 0, 0
        for idx, it in enumerate(s):
            if it not in s[left: idx]:
                if idx - left + 1> maxlen:
                    maxlen = idx - left + 1
            #在滑动窗口范围内中找出对应的首个字符的索引X，对应的新的左指针位置为X + 1
            else:
                left += s[left: idx].index(s[idx]) + 1
        return maxlen


x = Solution()
print(x.lengthOfLongestSubstring("pwwkew"))
