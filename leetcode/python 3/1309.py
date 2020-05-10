# 문제 링크: https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

class Solution:
    def freqAlphabets(self, s: str) -> str:
        for i in range(10, 27):
            s = s.replace(f'{i}#', chr(i + 96))
        for i in range(1, 10):
            s = s.replace(str(i), chr(i + 96))
        return s
