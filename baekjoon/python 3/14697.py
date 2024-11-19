# 문제 링크: https://www.acmicpc.net/problem/14697

A, B, C, N = map(int, input().split())

dp = [1] + [0] * N
for i in range(1, N + 1):
    for j in (A, B, C):
        if i >= j and dp[i - j]:
            dp[i] = 1

print(dp[N])
