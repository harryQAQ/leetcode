class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {')':'()', ']':'[', '}':'{'}
        for i in s:
            if mp.get(i, 0) == 0:
                stack.append(i)
            elif (not stack) or stack.pop != mp[i]:
                return False
        return not stack