# 문제 링크: https://leetcode.com/problems/largest-substring-between-two-equal-characters/

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        chars = [k for k, v in collections.Counter(s).items() if v > 1]
        return max(s.rfind(ch) - s.find(ch) - 1 for ch in chars) if chars else -1