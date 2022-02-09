# 문제 링크: https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        return [sum((x - qx) * (x - qx) + (y - qy) * (y - qy) <= qr * qr for x, y in points) for qx, qy, qr in queries]
