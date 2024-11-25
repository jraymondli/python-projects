from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dq = deque([(0, 0, 1)])
        nb = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        while dq:
            i, j, l = dq.popleft()
            if i < 0 or i == n or j < 0 or j == n: continue
            if grid[i][j]: continue
            if i == (n-1) and j == (n-1): return l
            grid[i][j] = 1
            for di, dj in nb:
                dq.append((i+di, j+dj, l+1))
        return -1
