# 문제 링크: https://leetcode.com/problems/replace-all-digits-with-characters/

class Solution:
    def replaceDigits(self, s: str) -> str:
        return ''.join(chr(ord(s[i - 1]) + int(s[i])) if i % 2 else s[i] for i in range(len(s)))