# 문제 링크: https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        matrix = [[0] * len(colSum) for _ in range(len(rowSum))]

        i = j = 0
        while i < len(rowSum) and j < len(colSum):
            matrix[i][j] = min(rowSum[i], colSum[j])
            rowSum[i] -= matrix[i][j]
            colSum[j] -= matrix[i][j]

            if rowSum[i] == 0:
                i += 1
            else:
                j += 1

        return matrix
