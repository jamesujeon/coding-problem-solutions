# 문제 링크: https://www.acmicpc.net/problem/1011

import sys
input = sys.stdin.readline

for _ in range(int(input())):
  x, y = map(int, input().split())
  d = y - x
  
  i = 1
  while i ** 2 < d:
    i += 1
  print(i * 2 - 1 - (1 if d <= i ** 2 - i else 0))