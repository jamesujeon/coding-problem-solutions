# 문제 링크: https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        return all(abs(word1.count(ch) - word2.count(ch)) <= 3 for ch in set(word1 + word2))