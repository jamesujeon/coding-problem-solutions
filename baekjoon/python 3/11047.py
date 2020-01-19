# 문제 링크: https://www.acmicpc.net/problem/11047

n, k = map(int, input().split())
a = sorted([int(input()) for _ in range(n)])

a = list(filter(lambda x: x <= k, a))
count = 0
while k > 0:
  x = a.pop()
  count += k // x
  k %= x

print(count)
