# 문제 링크: https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        return ' '.join(map(lambda s: s[:-1], sorted(s.split(), key=lambda s: s[-1])))