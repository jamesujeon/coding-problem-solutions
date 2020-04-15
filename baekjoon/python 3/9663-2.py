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

# 대칭 구조이므로 절반의 해에 2배를 곱해 구할 수 있다.
# 홀수인 경우, 홀수에 해당하는 경우를 추가적으로 구해야 한다.
# (수행 시간이 약 절반으로 줄어든다.)
for i in range(n // 2):
  b[0][i] = True
  bt(1)
  b[0][i] = False

c *= 2
if n % 2:
  b[0][n // 2 + 1] = True
  bt(1)

print(c)