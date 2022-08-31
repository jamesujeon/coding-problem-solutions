# 문제 링크: https://www.acmicpc.net/problem/2738

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

C = [[A[i][j] + B[i][j] for j in range(M)] for i in range(N)]

for i in range(N):
    print(' '.join(map(str, C[i])))
