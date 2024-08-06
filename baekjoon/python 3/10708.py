# 문제 링크: https://www.acmicpc.net/problem/10708

import sys
input = sys.stdin.readline

N, M = int(input()), int(input())
A = list(map(int, input().split()))
B = [list(map(int, input().split())) for _ in range(M)]

S = [0] * N
for i in range(M):
    for j in range(N):
        if B[i][j] == A[i]:
            S[j] += 1
        else:
            S[A[i] - 1] += 1

print(*S, sep='\n')
