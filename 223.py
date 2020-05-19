class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        #保证前面的矩形在左侧
        if A > E:
            return self.computeArea(E, F, G, H, A, B, C, D)
        sum = abs(A - C) * abs(B - D) + abs(E - G) * abs(H - F)
        if B >= H or F >= D or E >= C:
            return sum
        a = max(A, E)
        b = max(B, F)
        c = min(C, G)
        d = min(D, H)
        return sum - (c - a) * (d - b)
        