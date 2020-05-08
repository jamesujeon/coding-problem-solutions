# 문제 링크: https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        matrix = [[0 for _ in range(m)] for _ in range(n)]
        for ri, ci in indices:
            for i in range(m):
                matrix[ri][i] += 1
            for i in range(n):
                matrix[i][ci] += 1

        return sum(matrix[i][j] % 2 for i in range(n) for j in range(m))
