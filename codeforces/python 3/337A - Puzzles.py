# 문제 링크: http://codeforces.com/problemset/problem/337/A

n, _ = map(int, input().split())
counts = sorted(list(map(int, input().split())))

result = min(counts[i + n - 1] - counts[i] for i in range(len(counts) - n + 1))

print(result)