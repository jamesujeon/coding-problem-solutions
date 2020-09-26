# 문제 링크: https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counts, quarter = collections.Counter(arr), len(arr) / 4
        for n in counts:
            if counts[n] > quarter:
                return n
