# 문제 링크: https://leetcode.com/problems/regular-expression-matching/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s

        is_match_first = bool(s) and p[0] in (s[0], '.')

        if len(p) > 1 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (is_match_first and self.isMatch(s[1:], p))

        return is_match_first and self.isMatch(s[1:], p[1:])