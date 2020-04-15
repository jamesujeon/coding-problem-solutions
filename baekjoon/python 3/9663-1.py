# 문제 링크: https://www.acmicpc.net/problem/9663

n = int(input())

c, b = 0, [-1] * n
def f(y):
  if y == n:
    global c
    c += 1
    return

  for i in range(n):
    if any(i == b[j] or abs(i - b[j]) == abs(y - j) for j in range(y)):
      continue
    b[y] = i
    f(y + 1)

for i in range(n):
  b[0] = i
  f(1)

print(c)