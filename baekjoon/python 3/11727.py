# 문제 링크: https://www.acmicpc.net/problem/11727

n = int(input())

counts = {1: 1, 2: 3}
for i in range(3, n + 1):
  counts[i] = counts[i - 1] + counts[i - 2] * 2

print(counts[n] % 10007)