# 문제 링크: https://www.acmicpc.net/problem/9663

n = int(input())
c, b = 0, [-1] * n

def is_valid(y, x):
  for i in range(y):
    if x == b[i] or abs(x - b[i]) == abs(y - i):
      return False

  return True

def bt(y):
  if y == n:
    global c
    c += 1
    return

  for i in range(n):
    if is_valid(y, i):
      b[y] = i
      bt(y + 1)

for i in range(n):
  b[0] = i
  bt(1)

print(c)