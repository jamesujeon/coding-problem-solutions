# 문제 링크: https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        return sum(heights[i] != sorted_heights[i] for i in range(len(heights)))
