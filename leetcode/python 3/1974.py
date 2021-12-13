# 문제 링크: https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/

class Solution:
    def minTimeToType(self, word: str) -> int:
        seconds = 0
        for i in range(len(word)):
            diff = abs(ord(word[i]) - (ord(word[i - 1]) if i > 0 else 97))
            seconds += min(diff, 26 - diff) + 1

        return seconds