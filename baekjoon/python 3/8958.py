# 문제 링크: https://www.acmicpc.net/problem/8958

import sys

input()
for l in sys.stdin:
  print(sum(len(x) * (len(x) + 1) // 2 for x in l.strip().split('X') if x))