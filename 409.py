import collections

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # 1.统计各字符次数，eg:"ddsad":[3, 1, 1]
        count = collections.Counter(s).values()
        # 2.统计两两配对的字符总个数，eg: {"ddass":4,"ddsss":4}
        res = sum([item // 2 * 2 for item in count if item > 1])
        # 3.判断是否有没配对的单字符，有结果加一。
        return res if res == len(s) else res + 1