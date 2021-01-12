# 문제 링크: https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = 'aeiouAEIOU'
        a, b = s[:len(s) // 2], s[len(s) // 2:]
        return sum(ch in vowels for ch in a) == sum(ch in vowels for ch in b)