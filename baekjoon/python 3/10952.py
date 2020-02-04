# 문제 링크: https://www.acmicpc.net/problem/10952

import sys

for l in sys.stdin:
  s = sum(map(int, l.split()))
  if s == 0:
    break
  print(s)