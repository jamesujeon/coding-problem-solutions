# 문제 링크: https://leetcode.com/problems/complement-of-base-10-integer/

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return int(''.join('1' if b == '0' else '0' for b in bin(N)[2:]), 2)