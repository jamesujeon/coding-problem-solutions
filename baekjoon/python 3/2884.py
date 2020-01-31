# 문제 링크: https://www.acmicpc.net/problem/2884

h, m = map(int, input().split())

if m < 45:
  h = h - 1 if h > 0 else 23
  m += 15
else:
  m -= 45

print(h, m)