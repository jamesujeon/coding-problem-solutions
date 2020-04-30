# 문제 링크: https://www.acmicpc.net/problem/4153

import sys

for l in sys.stdin:
  a, b, c = sorted(map(int, l.split()))
  if a + b + c == 0:
    break
  print('right' if a**2 + b**2 == c**2 else 'wrong')