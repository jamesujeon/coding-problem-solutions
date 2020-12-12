# 문제 링크: https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0] * (n + 1)
        t[:3] = [0, 1, 1]
        for i in range(3, n + 1):
            t[i] = sum(t[i - 3:i])
        return t[n]