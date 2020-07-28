# 문제 링크: https://leetcode.com/problems/shuffle-string/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        l = list(s)
        for i, ch in zip(indices, s):
            l[i] = ch
        return ''.join(l)