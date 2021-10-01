# 문제 링크: https://leetcode.com/problems/roman-to-integer/

class Solution:
    symbols = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
        'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
    }

    def romanToInt(self, s: str) -> int:
        num = i = 0
        while i < len(s):
            if s[i:i + 2] in self.symbols:
                num += self.symbols[s[i:i + 2]]
                i += 2
            else:
                num += self.symbols[s[i]]
                i += 1

        return num