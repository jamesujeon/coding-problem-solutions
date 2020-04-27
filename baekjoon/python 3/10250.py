# 문제 링크: https://www.acmicpc.net/problem/10950

import sys
input = sys.stdin.readline

for _ in range(int(input())):
  h, _, n = map(int, input().split())
  f, r = n % h, n // h
  print(f'{h if f == 0 else f}{str(r if f == 0 else r + 1).zfill(2)}')