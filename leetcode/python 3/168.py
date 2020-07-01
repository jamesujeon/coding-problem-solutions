# 문제 링크: https://leetcode.com/problems/excel-sheet-column-title/

class Solution:
    def convertToTitle(self, n: int) -> str:
        column = ''
        while n:
            n -= 1
            column += chr(n % 26 + 65)
            n //= 26
        return column[::-1]