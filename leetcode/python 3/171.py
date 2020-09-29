# 문제 링크: https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, s: str) -> int:
        return sum((ord(ch) - 64) * (26 ** i) for i, ch in enumerate(s[::-1]))
