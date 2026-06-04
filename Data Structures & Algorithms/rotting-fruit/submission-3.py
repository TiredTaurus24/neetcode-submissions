from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_oranges = 0
        
        # Initialize the queue with all initial rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, col, time)
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        
        # If there are no fresh oranges, return 0
        if fresh_oranges == 0:
            return 0
        
        time_elapsed = 0
        
        # Multi-source BFS
        while queue:
            r, c, time = queue.popleft()
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # Mark as rotten
                    fresh_oranges -= 1
                    queue.append((nr, nc, time + 1))
                    time_elapsed = time + 1
        
        # If there are still fresh oranges left, return -1
        return time_elapsed if fresh_oranges == 0 else -1
