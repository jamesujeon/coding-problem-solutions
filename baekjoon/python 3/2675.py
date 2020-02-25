# 문제 링크: https://www.acmicpc.net/problem/2675

import sys

input()
for l in sys.stdin:
  n, s = l.split()
  n = int(n)
  print(''.join(n * c for c in s))