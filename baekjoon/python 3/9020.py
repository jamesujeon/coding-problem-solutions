# 문제 링크: https://www.acmicpc.net/problem/9020

import sys
input = sys.stdin.readline

n = 10000
s = [False, False] + [True] * (n - 1)
for i in range(2, int(n ** .5) + 1):
  for j in range(i * 2, n + 1, i):
    if s[j]:
      s[j] = False

for _ in range(int(input())):
  n = int(input())
  for i in range(n // 2, n + 1):
    if s[i] and s[n - i]:
      print(n - i, i)
      break
