# 문제 링크: https://www.acmicpc.net/problem/2447

n = int(input())
s = [[' ' for _ in range(n)] for _ in range(n)]

def f(n, y, x):
  if n == 3:
    for i in range(3):
      s[y][x + i] = '*'
    s[y + 1][x] = s[y + 1][x + 2] = '*'
    for i in range(3):
      s[y + 2][x + i] = '*'
    return

  n = n // 3
  for i in range(3):
    for j in range(3):
      if i != 1 or j != 1:
        f(n, y + i * n, x + j * n)

f(n, 0, 0)

for l in s:
  print(''.join(l))