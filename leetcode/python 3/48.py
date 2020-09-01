# 문제 링크: https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                k, l = n - i - 1, n - j - 1 
                matrix[i][j], matrix[j][k] = matrix[j][k], matrix[i][j]
                matrix[l][i], matrix[i][j] = matrix[i][j], matrix[l][i]
                matrix[k][l], matrix[l][i] = matrix[l][i], matrix[k][l]