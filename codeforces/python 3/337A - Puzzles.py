# 문제 링크: http://codeforces.com/problemset/problem/337/A

n, _ = map(int, input().split())
counts = sorted(list(map(int, input().split())))

result = 1000
for i in range(len(counts) - n + 1):
  result = min(result, counts[i + n - 1] - counts[i])

print(result)