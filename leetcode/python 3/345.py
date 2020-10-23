# 문제 링크: https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
        result = list(s)
        indexes = [i for i in range(len(s)) if s[i] in 'aeiouAEIOU']
        for i, j in zip(indexes, indexes[::-1]):
            result[i] = s[j]
        return ''.join(result)
