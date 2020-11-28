# 문제 링크: https://leetcode.com/problems/count-sorted-vowel-strings/

class Solution:
    def countVowelStrings(self, n: int) -> int:
        counts = [1] * 5
        for _ in range(n - 1):
            counts = [sum(counts[:i + 1]) for i in range(5)]
        return sum(counts)