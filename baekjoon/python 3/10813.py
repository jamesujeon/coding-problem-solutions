# 문제 링크: https://www.acmicpc.net/problem/10813

N, M = map(int, input().split())
b = list(range(1, N + 1))
for _ in range(M):
    i, j = map(int, input().split())
    b[i - 1], b[j - 1] = b[j - 1], b[i - 1]

print(*b)
