# 문제 링크: https://leetcode.com/problems/matrix-block-sum/

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        def block_sum(i: int, j: int) -> int:
            i_range = range(max(0, i - K), min(m, i + K + 1))
            j_range = range(max(0, j - K), min(n, j + K + 1))
            return sum(mat[i][j] for i in i_range for j in j_range)

        return [[block_sum(i, j) for j in range(n)] for i in range(m)]
