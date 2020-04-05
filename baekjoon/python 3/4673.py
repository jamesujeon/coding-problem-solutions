# 문제 링크: https://www.acmicpc.net/problem/4673

def d(n):
  return n + sum(i for i in map(int, str(n)))

n = 10000
sn = [1] * (n + 1)
for i in range(n):
  dn = d(i + 1)
  if dn <= n:
    sn[d(i + 1)] = 0

for i in range(n):
  if sn[i + 1]:
    print(i + 1)
