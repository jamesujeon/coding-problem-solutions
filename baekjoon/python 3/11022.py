# 문제 링크: https://www.acmicpc.net/problem/11022

import sys

input()
for i, l in enumerate(sys.stdin.readlines()):
  a, b = map(int, l.split())
  print(f'Case #{i + 1}: {a} + {b} = {a + b}')