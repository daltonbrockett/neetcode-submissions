class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited = set()
        rows, columns = len(grid), len(grid[0])
        islands = 0

        def bfs(row, column):
            deq = deque()
            deq.append((row,column))
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            while deq:
                r, c = deq.popleft()
                for dirX, dirY in directions:
                    x = dirX + r
                    y = dirY + c
                    if 0 <= x < rows and 0 <= y <columns and grid[x][y] == '1' and (x, y) not in visited:
                        deq.append((x, y))
                        visited.add((x,y))

        for row in range(0, rows):
                    for column in range(0, columns):
                        point = grid[row][column]
                        if point == '1' and (row, column) not in visited:
                            visited.add((row, column))
                            bfs(row, column)
                            islands += 1
        return islands
                    