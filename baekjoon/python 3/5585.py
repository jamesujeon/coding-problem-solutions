# 문제 링크: https://www.acmicpc.net/problem/5585

n = 1000 - int(input())

count = 0
for i in [500, 100, 50, 10, 5, 1]:
  if n == 0:
    break

  count += n // i
  n %= i

print(count)
