# 문제 링크: https://www.acmicpc.net/problem/5575

for a in [list(map(int, input().split())) for _ in range(3)]:
  a = [a[3] - a[0], a[4] - a[1], a[5] - a[2]]
  if a[2] < 0:
    a[2] += 60
    a[1] -= 1
  if a[1] < 0:
    a[1] += 60
    a[0] -= 1
  print(' '.join(map(str, a)))