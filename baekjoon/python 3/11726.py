# 문제 링크: https://www.acmicpc.net/problem/11726

n = int(input())

counts = [1, 2]
for i in range(2, n):
  counts.append(counts[i - 1] + counts[i - 2])

print(counts[n - 1] % 10007)