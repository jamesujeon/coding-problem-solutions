# 문제 링크: https://www.acmicpc.net/problem/1193

x = int(input())

i = 1
while i * (i + 1) / 2 < x:
  i += 1

d = x - i * (i - 1) // 2
n = i - d + 1
print(f'{n}/{d}' if i % 2 else f'{d}/{n}')