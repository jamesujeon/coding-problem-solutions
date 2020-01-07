# 문제 링크: https://www.acmicpc.net/problem/1003

ns = [int(input()) for _ in range(int(input()))]

fns = {0: (0, 1, 0), 1: (1, 0, 1)}
def fn(n):
  if n in fns:
    return fns[n]
  fns[n] = tuple(n1 + n2 for n1, n2 in zip(fn(n - 1), fn(n - 2)))
  return fns[n]

for n in ns:
  print(' '.join(map(str, fn(n)[1:])))