# 문제 링크: https://www.acmicpc.net/problem/2193

n = int(input())

counts = [0, 1]
for i in range(2, n + 1):
  counts.append(counts[i - 1] + counts[i - 2])

print(counts[-1])