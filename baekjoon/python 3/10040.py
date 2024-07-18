# 문제 링크: https://www.acmicpc.net/problem/10040

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
B = [int(input()) for _ in range(M)]

V = [0] * N
for b in B:
    for i in range(N):
        if A[i] <= b:
            V[i] += 1
            break

print(V.index(max(V)) + 1)
