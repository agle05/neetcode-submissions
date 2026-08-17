# Approach could be to search through array row by row, finding where there is "land", and counting the islands. When you see a 1, check if there is a 1 near it (top/right/bottom/left). This approach would be O(n2) complexity.

# Another approach could be: when you find a 1, run a DFS or BFS search on the grid where you find adjacent 1's, then secondary adjacent 1's, until you understand where the entire island is. Then rule out those cells. But how?

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0

        rows, cols = len(grid), len(grid[0])

        def flood(row, col) -> None:
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != '1': return
            grid[row][col] = '0'
            flood(row-1, col)
            flood(row, col+1)
            flood(row+1, col)
            flood(row, col-1)

        islandCount = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    islandCount += 1
                    flood(i, j)

        return islandCount
