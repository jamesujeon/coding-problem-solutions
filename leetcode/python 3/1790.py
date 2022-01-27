# 문제 링크: https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        return set(s1) == set(s2) and sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2)) in (0, 2)