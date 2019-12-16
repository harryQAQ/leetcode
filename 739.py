class Solution:
    def dailyTemperatures(self, T: list) -> list:
        stack, res = [], [0] * len(T)
        for idx, temp in enumerate(T):
            while stack and stack[-1][1] < temp:
                st, _ = stack.pop()
                res[st] = idx - st
            stack.append([idx, temp])
        return res

x = Solution()
print(x.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))

