# 문제 링크: https://www.acmicpc.net/problem/2292

n = int(input())

s, i = 1, 1
while s < n:
  s += i * 6
  i += 1

print(i)