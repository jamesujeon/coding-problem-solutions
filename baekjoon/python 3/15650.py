# 문제 링크: https://www.acmicpc.net/problem/15650

n, m = map(int, input().split())

s = []
def f(i):
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for j in range(i + 1, n + 1):
    s.append(j)
    f(j)
    s.pop()

f(0)