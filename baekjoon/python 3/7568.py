# 문제 링크: https://www.acmicpc.net/problem/7568

import sys

n = int(input())
xy = [tuple(map(int, l.split())) for l in sys.stdin.readlines()]

rankings = [1] * n
for i in range(len(xy)):
  for x, y in xy:
    if xy[i][0] < x and xy[i][1] < y:
      rankings[i] += 1

print(' '.join(map(str, rankings)))