# 문제 링크: https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges = [range(start, end + 1) for start, end in ranges]

        return all(any(x in r for r in ranges) for x in range(left, right + 1))
