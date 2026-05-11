class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        seen = set()
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def bfs(r, c):
            queue = collections.deque()
            queue.append((r,c))
            while queue:
                r,c = queue.popleft()
                seen.add((r, c))
                for dr, dc in dirs:
                    newR, newC = r + dr, c + dc
                    if ((newR, newC) not in seen
                        and newR >= 0 and newR < len(grid)
                        and newC >= 0 and newC < len(grid[0])
                        and grid[newR][newC] != '0'):
                        
                        queue.append((newR, newC))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '0' or (r,c) in seen:
                    continue
                bfs(r, c)
                islands += 1
        return islands