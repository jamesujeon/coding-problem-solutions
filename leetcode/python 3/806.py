# 문제 링크: https://leetcode.com/problems/number-of-lines-to-write-string/

class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        lines, units = 1, 0
        for letter in S:
            width = widths[ord(letter) - 97]
            if units + width <= 100:
                units += width
            else:
                lines += 1
                units = width
        return [lines, units]