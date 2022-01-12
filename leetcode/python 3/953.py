# 문제 링크: https://leetcode.com/problems/verifying-an-alien-dictionary/

from functools import cmp_to_key

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = {l: i for i, l in enumerate(order)}

        def cmp(s1: str, s2: str) -> int:
            for l1, l2 in zip(s1, s2):
                if l1 != l2:
                    return order[l1] - order[l2]
            return len(s1) - len(s2)

        return words == sorted(words, key=cmp_to_key(cmp))