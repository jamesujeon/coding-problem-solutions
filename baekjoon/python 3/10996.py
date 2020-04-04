# 문제 링크: https://www.acmicpc.net/problem/10996

n = int(input())
r = range(n)
s = ['*', ' ']
for _ in r:
  print(''.join(s[i % 2 != 0] for i in r))
  if n > 1:
    print(''.join(s[i % 2 == 0] for i in r))