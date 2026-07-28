class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        visited = set()

        islands = 0

        def bfs(r, c):

            queue = [(r, c)]

            visited.add((r, c))

            while queue:

                row, col = queue.pop(0)

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and (r, c) not in visited:
                        visited.add((r, c))
                        if grid[r][c] == "1":
                            queue.append((r, c))

        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and grid[row][col] == "1":
                    bfs(row, col)
                    islands += 1

        return islands
                    
        


        