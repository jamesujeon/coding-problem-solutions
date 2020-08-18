# 문제 링크: https://leetcode.com/problems/matrix-block-sum/

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        dp = [[0] * (n + 1) for _ in range(m)]
        dp[0][0] = mat[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + mat[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + mat[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + mat[i][j]

        def get_answer(i: int, j: int) -> int:
            i1, i2 = i - K, min(m - 1, i + K)
            j1, j2 = j - K, min(n - 1, j + K)

            answer = dp[i2][j2]
            if i1 > 0:
                answer -= dp[i1 - 1][j2]
            if j1 > 0:
                answer -= dp[i2][j1 - 1]
            if i1 > 0 and j1 > 0:
                answer += dp[i1 - 1][j1 - 1]
            return answer

        return [[get_answer(i, j) for j in range(n)] for i in range(m)]