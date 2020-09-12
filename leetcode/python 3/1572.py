# 문제 링크: https://leetcode.com/problems/matrix-diagonal-sum/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        c = mat[n // 2][n // 2] if n % 2 else 0
        s1 = sum(mat[i][i] for i in range(n))
        s2 = sum(mat[n - i - 1][i] for i in range(n))
        return s1 + s2 - c
