# 문제 링크: https://www.acmicpc.net/problem/9663

n = int(input())
c, b = 0, [[False] * n for _ in range(n)]

def is_valid(y, x):
  for i in range(y):
    if b[i][x]:
      return False

  for i in range(y):
    bi = x - y + i
    if bi >= 0 and b[i][bi]:
      return False

  for i in range(y):
    si = x + y - i
    if si < n and b[i][si]:
      return False

  return True

def bt(y):
  if y == n:
    global c
    c += 1
    return

  for i in range(n):
    if is_valid(y, i):
      b[y][i] = True
      bt(y + 1)
      b[y][i] = False

for i in range(n):
  b[0][i] = True
  bt(1)
  b[0][i] = False

print(c)