# 문제 링크: https://leetcode.com/problems/toeplitz-matrix/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(matrix[i][:-1] == matrix[i + 1][1:] for i in range(len(matrix) - 1))