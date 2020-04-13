# 문제 링크: https://www.acmicpc.net/problem/15652

n, m = map(int, input().split())

s = []
def f(i):
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for j in range(i, n + 1):
    s.append(j)
    f(j)
    s.pop()

f(1)