# 문제 링크: https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1), len(word2))
        return ''.join(word1[i] + word2[i] for i in range(min_len)) + word1[min_len:] + word2[min_len:]