# 문제 링크: https://leetcode.com/problems/uncommon-words-from-two-sentences/

from collections import Counter

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        A, B = Counter(A.split()), Counter(B.split())
        a_set = set(word for word, count in A.items() if count == 1 and word not in B)
        b_set = set(word for word, count in B.items() if count == 1 and word not in A)
        return list(a_set ^ b_set)