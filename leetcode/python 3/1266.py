# 문제 링크: https://leetcode.com/problems/minimum-time-visiting-all-points/

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        seconds = 0
        for i in range(len(points) - 1):
            cp, np = points[i], points[i + 1]
            seconds += max(abs(np[0] - cp[0]), abs(np[1] - cp[1]))
        return seconds
