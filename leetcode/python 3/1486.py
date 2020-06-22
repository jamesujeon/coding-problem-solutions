# 문제 링크: https://leetcode.com/problems/xor-operation-in-an-array/

from functools import reduce

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        return reduce(lambda a, b: a^b, [start + i * 2 for i in range(n)])