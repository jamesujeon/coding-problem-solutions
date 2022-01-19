# 문제 링크: https://leetcode.com/problems/check-if-it-is-a-straight-line/

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def get_slope(i: int) -> float:
            dx = coordinates[i][0] - coordinates[i - 1][0]
            return (coordinates[i][1] - coordinates[i - 1][1]) / dx if dx != 0 else float('inf')

        slope = get_slope(1)
        return all(get_slope(i) == slope for i in range(2, len(coordinates)))