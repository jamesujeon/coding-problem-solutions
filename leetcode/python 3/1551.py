# 문제 링크: https://leetcode.com/problems/minimum-operations-to-make-array-equal/

class Solution:
    def minOperations(self, n: int) -> int:
        return ((n + 1) // 2) * (n // 2)
