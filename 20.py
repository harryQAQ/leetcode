class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {')':'(', ']':'[', '}':'{'}
        for i in s:
            if mp.get(i, 0) == 0: #只要是左括号就压入栈中
                stack.append(i)
            elif (not stack) or stack.pop != mp[i]: #右括号，则要匹配栈顶的左括号，若不匹配或者栈空则返回false
                return False
        return not stack