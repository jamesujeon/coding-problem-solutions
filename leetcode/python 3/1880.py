# 문제 링크: https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def convert(word: str) -> int:
            return int(''.join(str(ord(ch) - 97) for ch in word))

        return convert(firstWord) + convert(secondWord) == convert(targetWord)