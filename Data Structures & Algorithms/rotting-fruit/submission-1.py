# Key idea: keep a queue of rotten oranges. For each round, for each in the queue, rot the adjacent oranges. If the queue becomes empty, then we know there are no more oranges that can be rotted by adjacency. Finally, run one more check over the grid, and if there are still fresh fruit remaining, return -1, otherwise return the number of rounds.

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return

        queue = deque()
        rows, cols = len(grid), len(grid[0])
        minutes = 0

        # Initial queue population
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append([i, j])

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if row+1 < rows and grid[row+1][col] == 1: 
                    grid[row+1][col] = 2
                    queue.append([row+1, col])
                if row-1 >= 0 and grid[row-1][col] == 1: 
                    grid[row-1][col] = 2
                    queue.append([row-1, col])
                if col+1 < cols and grid[row][col+1] == 1: 
                    grid[row][col+1] = 2
                    queue.append([row, col+1])
                if col-1 >= 0 and grid[row][col-1] == 1: 
                    grid[row][col-1] = 2
                    queue.append([row, col-1])

            if queue:
                minutes += 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1

        return minutes

