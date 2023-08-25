# 문제 링크: https://www.acmicpc.net/problem/26432

import sys
input = sys.stdin.readline

for c in range(1, int(input()) + 1):
    M, N, P = map(int, input().split())
    S = [list(map(int, input().split())) for _ in range(M)]

    max_S = [0] * N
    for i in range(M):
        for j in range(N):
            max_S[j] = max(S[i][j], max_S[j])
    result = sum(max_S[j] - S[P - 1][j] for j in range(N))

    print(f"Case #{c}: {result}")
