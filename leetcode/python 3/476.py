# 문제 링크: https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        return int(''.join('1' if b == '0' else '0' for b in bin(num)[2:]), 2)