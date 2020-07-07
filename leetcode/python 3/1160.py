# 문제 링크: https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        chars = Counter(chars)
        for word in words:
            word_chars = Counter(word)
            if all(c in chars and word_chars[c] <= chars[c] for c in word_chars):
                result += len(word)
        return result