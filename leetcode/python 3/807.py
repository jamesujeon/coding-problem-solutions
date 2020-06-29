# 문제 링크: https://leetcode.com/problems/max-increase-to-keep-city-skyline/

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows = range(len(grid))
        cols = range(len(grid[0]))
        lr = [max(row) for row in grid]
        tb = [max(grid[i][j] for i in rows) for j in cols]

        return sum(min(lr[i], tb[j]) - grid[i][j] for i in rows for j in cols)