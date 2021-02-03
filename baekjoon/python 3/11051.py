# 문제 링크: https://www.acmicpc.net/problem/11051

n, k = map(int, input().split())

dp = [[1] * (k + 1) for _ in range(n + 1)]
for i in range(n + 1):
    for j in range(min(i, k) + 1):
        if j > 0 and i != j:
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

print(dp[n][k] % 10007)