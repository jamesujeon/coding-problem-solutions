# 문제 링크: https://www.acmicpc.net/problem/3009

import sys
input = sys.stdin.readline

x = y = 0
for i, j in [map(int, input().split()) for _ in range(3)]:
  x ^= i
  y ^= j

print(x, y)