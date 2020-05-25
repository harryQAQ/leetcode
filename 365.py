from collections import deque

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        q = deque()
        visit = set()
        #init
        q.append((0, 0))
        visit.add((0, 0))
        while q:
            x_cur, y_cur = q.popleft()
            if x_cur == z or y_cur ==z or x_cur + y_cur == z:
                return True
            for (next_x, next_y) in [(x_cur, 0), (0, y_cur), (x_cur, y), (x, y_cur), (x, y_cur + x_cur - x) if x_cur + y_cur >= x else (x_cur + y_cur, 0), (x_cur + y_cur - y, y) if x_cur + y_cur >= y else (0, x_cur + y_cur)]:
                if (next_x, next_y) not in visit:
                    visit.add((next_x, next_y))
                    q.append((next_x, next_y))
        return False
