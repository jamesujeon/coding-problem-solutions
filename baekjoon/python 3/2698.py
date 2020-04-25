# 문제 링크: https://www.acmicpc.net/problem/2698

import sys
input = sys.stdin.readline

dp = [[[0] * 2 for _ in range(100)] for _ in range(101)]
dp[1][0][0] = dp[1][0][1] = 1
for n in range(2, 101):
  for k in range(n):
    dp[n][k][0] = dp[n - 1][k][0] + dp[n - 1][k][1]
    dp[n][k][1] = dp[n - 1][k][0] + (dp[n - 1][k - 1][1] if k > 0 else 0)

for _ in range(int(input())):
  n, k = map(int, input().split())
  print(dp[n][k][0] + dp[n][k][1])