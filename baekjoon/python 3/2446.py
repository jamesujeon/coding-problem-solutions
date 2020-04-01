# 문제 링크: https://www.acmicpc.net/problem/2446

n = int(input())
for i in range(-n + 1, n):
  print(' ' * (n - abs(i) - 1) + '*' * (2 * abs(i) + 1))