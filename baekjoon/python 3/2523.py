# 문제 링크: https://www.acmicpc.net/problem/2523

n = int(input())
for i in range(1, n + 1):
  print('*' * i)
for i in range(n - 1, 0, -1):
  print('*' * i)