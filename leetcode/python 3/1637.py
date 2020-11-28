# 문제 링크: https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_points = sorted(x for x, y in points)
        widths = [x_points[i + 1] - x_points[i] for i in range(len(x_points) - 1)]
        return max(widths) if widths else 0