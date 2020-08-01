# 문제 링크: https://leetcode.com/problems/keyboard-row/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        def validate(word: str) -> bool:
            word = word.lower()
            row = next(row for row in rows if word[0] in row)
            return all(letter in row for letter in word)

        return [word for word in words if validate(word)]
