# 문제 링크: https://www.acmicpc.net/problem/11021

import sys

input()
for i, l in enumerate(sys.stdin):
  print(f'Case #{i + 1}: {sum(map(int, l.split()))}')