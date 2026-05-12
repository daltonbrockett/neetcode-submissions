class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
            rows, cols = len(grid), len(grid[0])
            seen = set()
            dirs = [[0,1], [0,-1], [1,0], [-1, 0]]
            maxArea = 0
            def bfs(r, c):
                q = collections.deque()
                q.append((r,c))
                seen.add((r, c))
                area = 0
                while q:
                    r, c = q.popleft()
                    area += 1
                    for dr, dc in dirs:
                        newR, newC = r + dr, c + dc
                        if (newR >= 0 and newR < rows
                            and newC >= 0 and newC < cols
                            and grid[newR][newC] == 1
                            and (newR, newC) not in seen):
                            q.append((newR, newC))
                            seen.add((newR, newC))
                return area

            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 0 or (r,c) in seen:
                        continue
                    maxArea = max(maxArea, bfs(r,c))
            return maxArea
                    