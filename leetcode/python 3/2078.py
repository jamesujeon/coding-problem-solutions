# 문제 링크: https://leetcode.com/problems/two-furthest-houses-with-different-colors/

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        for i in range(len(colors) - 1):
            if colors[i] != colors[-1] or colors[-(i + 1)] != colors[0]:
                return len(colors) - i - 1

        return 0