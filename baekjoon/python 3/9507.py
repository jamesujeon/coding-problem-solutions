# 문제 링크: https://www.acmicpc.net/problem/2698

import sys
input = sys.stdin.readline

dp = [1, 1, 2, 4]
for n in range(4, 68):
  dp.append(sum(dp[n - 4:]))

for _ in range(int(input())):
  print(dp[int(input())])