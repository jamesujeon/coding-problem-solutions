# 문제 링크: https://leetcode.com/problems/maximum-number-of-balloons/

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text = collections.Counter(text)
        return min(text[ch] // 2 if ch in "lo" else text[ch] for ch in "balon")