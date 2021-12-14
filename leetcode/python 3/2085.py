# 문제 링크: https://leetcode.com/problems/count-common-words-with-one-occurrence/

from collections import Counter

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words1 = Counter(words1)
        words2 = Counter(words2)

        return sum(words1[word] == words2[word] == 1 for word in words1)