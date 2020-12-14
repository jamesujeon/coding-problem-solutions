# 문제 링크: https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = bin(n)[2:]
        return all(n[i] != n[i + 1] for i in range(len(n) - 1))