# 문제 링크: https://www.acmicpc.net/problem/2577

from functools import reduce

n = str(reduce(lambda x, y: x * y, [int(input()) for _ in range(3)]))

m = [0] * 10
for i in n:
  m[int(i)] += 1

for i in m:
  print(i)