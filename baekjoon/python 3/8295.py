# 문제 링크: https://www.acmicpc.net/problem/8295

n, m, p = map(int, input().split())

print(sum((n - i + 1) * (m - j + 1) for i in range(1, n + 1) for j in range(1, m + 1) if (i + j) * 2 >= p))
