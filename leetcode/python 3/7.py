# 문제 링크: https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)[::-1]
        if x[-1] == '-':
            x = x[-1] + x[:-1]
        x = int(x)
        return x if -2**31 <= x <= 2**31 - 1 else 0
