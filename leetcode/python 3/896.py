# 문제 링크: https://leetcode.com/problems/monotonic-array/

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return A == sorted(A) or A == sorted(A, reverse=True)
