# 문제 링크: https://leetcode.com/problems/matrix-block-sum/

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = mat[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + mat[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + mat[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + mat[i][j]

        def get_answer(i: int, j: int) -> int:
            answer = dp[min(m - 1, i + K)][min(n - 1, j + K)]
            if i - K > 0:
                answer -= dp[i - K - 1][min(n - 1, j + K)]
            if j - K > 0:
                answer -= dp[min(m - 1, i + K)][j - K - 1]
            if i - K > 0 and j - K > 0:
                answer += dp[i - K - 1][j - K - 1]
            return answer

        return [[get_answer(i, j) for j in range(n)] for i in range(m)]