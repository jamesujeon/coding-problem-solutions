# 문제 링크: https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def convert(word: str) -> str:
            p = {}
            return [p.setdefault(letter, len(p)) for letter in word]

        pattern = convert(pattern)
        return [word for word in words if convert(word) == pattern]