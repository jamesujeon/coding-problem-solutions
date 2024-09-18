# 문제 링크: https://www.acmicpc.net/problem/11680

N, M = map(int, input().split())
d = [0] * (N + M)
for i in range(N):
    for j in range(M):
        d[i + j] += 1

m = max(d)
for i in range(len(d)):
    if d[i] == m:
        print(i + 2)
