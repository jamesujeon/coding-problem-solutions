# 문제 링크: https://leetcode.com/problems/goat-latin/

class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        words = S.split()
        for i, word in enumerate(words):
            if word[0].lower() not in vowels:
                word += word[0]
                word = word[1:]
            word += 'ma' + 'a' * (i + 1)
            words[i] = word
        return ' '.join(words)