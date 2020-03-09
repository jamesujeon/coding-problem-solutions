# 문제 링크: https://www.acmicpc.net/problem/4344

for _ in range(int(input())):
  l = list(map(int, input().split()))
  a = sum(l[1:]) / l[0]
  print('%.3f%%' % (sum(i > a for i in l[1:]) / l[0] * 100))