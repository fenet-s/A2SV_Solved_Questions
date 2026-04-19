from typing import List
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        r, c = 0, cols - 1
        count = 0
        
        while r < rows and c >= 0:
            if grid[r][c] < 0:
                count += (rows - r)
                c -= 1
            else:
                r += 1
        
        return count