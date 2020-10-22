# 문제 링크: https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        repeating_chars = set()
        for i, ch in enumerate(s):
            if ch not in repeating_chars:
                if s.count(ch) == 1:
                    return i
                else:
                    repeating_chars.add(ch)
        return -1