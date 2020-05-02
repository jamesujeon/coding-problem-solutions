# 문제 링크: https://www.acmicpc.net/problem/4948

import sys

n = 246912
s = [False, False] + [True] * (n - 1)
for i in range(2, int(n ** .5) + 1):
  if s[i]:
    for j in range(i * 2, n + 1, i):
      s[j] = False

for l in sys.stdin:
  n = int(l)
  if n == 0:
    break
  print(sum(s[i] for i in range(n + 1, n * 2 + 1)))