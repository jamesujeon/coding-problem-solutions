# 문제 링크: https://leetcode.com/problems/maximum-number-of-words-you-can-type/

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        return sum(all(l not in w for l in brokenLetters) for w in text.split())