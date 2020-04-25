# 문제 링크: https://www.acmicpc.net/problem/2210

d = [input().split() for _ in range(5)]

n = set()
def move(y, x, s):
  if len(s) == 6:
    n.add(s)
    return

  if y > 0:
    move(y - 1, x, s + d[y - 1][x])
  if x > 0:
    move(y, x - 1, s + d[y][x - 1])
  if y < 4:
    move(y + 1, x, s + d[y + 1][x])
  if x < 4:
    move(y, x + 1, s + d[y][x + 1])

for i in range(5):
  for j in range(5):
    move(i, j, d[i][j])

print(len(n))