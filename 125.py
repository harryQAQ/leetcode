class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s: return True
        left, right = 0, len(s) - 1
        case = ord('A') - ord('a')

        while left < right:
            while left < right and not self.judge(s[left]): left += 1
            while left < right and not self.judge(s[right]): right -= 1
            #str与int计算 必须要转为ascii码，而即使小写也要转，如果是一个大写一个小写，直接取字符就无法比较了
            s_left = ord(s[left]) - case if 'A' <= s[left] <= 'Z' else s[left]
            s_right = ord(s[right]) - case if 'A' <= s[right] <= 'Z' else s[right]

            if s_left != s_right:
                return False
            left += 1
            right -= 1
        return True

    def judge(self, s):
        return '0' <= s <= '9' or 'a' <= s <= 'z' or 'A' <= s <= 'Z'




x = Solution()
print(x.isPalindrome("A man, a plan, a canal: Panama"))