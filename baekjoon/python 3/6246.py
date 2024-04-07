# 문제 링크: https://www.acmicpc.net/problem/6246

import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

B = [1] * N
for _ in range(Q):
    L, I = map(int, input().split())
    for i in range(L - 1, N, I):
        B[i] = 0

print(sum(B))
