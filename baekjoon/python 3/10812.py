# 문제 링크: https://www.acmicpc.net/problem/10812

N, M = map(int, input().split())
b = list(range(1, N + 1))
for _ in range(M):
    i, j, k = map(int, input().split())
    b[i - 1:j] = b[k - 1:j] + b[i - 1:k - 1]

print(*b)
