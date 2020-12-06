# 문제 링크: https://leetcode.com/problems/binary-gap/

class Solution:
    def binaryGap(self, n: int) -> int:
        n = bin(n)[2:]
        indexes = [i for i in range(len(n)) if n[i] == '1']
        if len(indexes) < 2:
            return 0
        return max(indexes[i + 1] - indexes[i] for i in range(len(indexes) - 1))