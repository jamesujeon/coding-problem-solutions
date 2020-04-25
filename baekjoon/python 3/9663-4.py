# 문제 링크: https://www.acmicpc.net/problem/9663

n = int(input())

mark_y = [False] * n
mark_lu = [False] * (n * 2 - 1)
mark_ru = [False] * (n * 2 - 1)
def mark(y, x, flag):
  mark_y[x] = flag
  mark_lu[y - x + n - 1] = flag
  mark_ru[y + x] = flag

count = 0
def bt(y):
  if y == n:
    global count
    count += 1
    return

  for i in range(n):
    if mark_y[i] or mark_lu[y - i + n - 1] or mark_ru[y + i]:
      continue

    mark(y, i, True)
    bt(y + 1)
    mark(y, i, False)

# 대칭 구조이므로 절반의 해에 2배를 곱해 구할 수 있다.
# 홀수인 경우, 홀수에 해당하는 경우를 추가적으로 구해야 한다.
# (수행 시간이 약 절반으로 줄어든다.)
for i in range(n // 2):
  mark(0, i, True)
  bt(1)
  mark(0, i, False)

count *= 2
if n % 2:
  mark(0, n // 2, True)
  bt(1)

print(count)