# 문제 링크: https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s, t = Counter(s), Counter(t)
        for char, count in t.items():
            if char in s:
                s[char] -= count
        return sum(count for count in s.values() if count > 0)