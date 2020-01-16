# 문제 링크: https://www.acmicpc.net/problem/2839

n = int(input())

count = -1
for x in reversed(range(n // 5 + 1)):
  y = n - (5 * x)
  if y >= 0 and y % 3 == 0:
    count = x + int(y / 3)
    break

print(count)