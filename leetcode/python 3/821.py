# 문제 링크: https://leetcode.com/problems/shortest-distance-to-a-character/

class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        c_indexes = [i for i, ch in enumerate(S) if ch == C]
        return [0 if i in c_indexes else min(abs(ci - i) for ci in c_indexes) for i in range(len(S))]