# 문제 링크: https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [r[0] for r in sorted([(i, mat[i].count(1)) for i in range(len(mat))], key=lambda x: x[1])[:k]]