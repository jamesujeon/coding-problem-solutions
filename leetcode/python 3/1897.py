# 문제 링크: https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

from collections import Counter

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        return all(count % len(words) == 0 for count in Counter(''.join(words)).values())