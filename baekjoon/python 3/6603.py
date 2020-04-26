# 문제 링크: https://www.acmicpc.net/problem/6603

import sys

result = []
def f(index, k, s):
  if len(result) == 6:
    print(' '.join(map(str, result)))
    return

  for i in range(index, k):
    result.append(s[i])
    f(i + 1, k, s)
    result.pop()

for l in sys.stdin:
  s = l.split()
  if s.pop(0) == '0':
    break

  f(0, len(s), s)
  print()