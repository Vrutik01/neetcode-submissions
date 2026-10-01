class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        INF = (2 ** 31) - 1
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c, 0])

        while q:
            r, c, dis = q.popleft()

            for dr, dc in directions:
                row = dr + r
                col = dc + c

                if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == INF:
                    grid[row][col] = dis + 1
                    q.append([row, col, dis + 1])