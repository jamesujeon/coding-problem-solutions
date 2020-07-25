# 문제 링크: https://leetcode.com/problems/island-perimeter/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def get_perimeter(grid: List[List[int]], i: int, j: int) -> int:
            if grid[i][j] == 0:
                return 0
            perimeter = 0
            perimeter += i == 0 or grid[i - 1][j] == 0
            perimeter += j == 0 or grid[i][j - 1] == 0
            perimeter += i == rows - 1 or grid[i + 1][j] == 0
            perimeter += j == cols - 1 or grid[i][j + 1] == 0
            return perimeter

        return sum(get_perimeter(grid, i, j) for i in range(rows) for j in range(cols))