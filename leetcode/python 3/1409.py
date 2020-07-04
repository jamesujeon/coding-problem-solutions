# 문제 링크: https://leetcode.com/problems/queries-on-a-permutation-with-key/

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = list(range(1, m + 1))
        positions = []
        for query in queries:
            positions.append(P.index(query))
            P.insert(0, P.pop(positions[-1]))
        return positions