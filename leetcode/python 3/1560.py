# 문제 링크: https://leetcode.com/problems/most-visited-sector-in-a-circular-track/

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        first, last = rounds[0], rounds[-1]
        if first <= last:
            return [*range(first, last + 1)]
        else:
            return [*range(1, last + 1), *range(first, n + 1)]