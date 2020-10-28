# 문제 링크: https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        power = 1
        while power < n:
            power *= 2
        return power == n if n != 1 else True