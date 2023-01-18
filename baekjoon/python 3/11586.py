# 문제 링크: https://www.acmicpc.net/problem/11586

import sys
input = sys.stdin.readline

N = int(input())
M = [input().strip() for _ in range(N)]
K = int(input())

if K == 1:
    for i in range(N):
        print(M[i])
elif K == 2:
    for i in range(N):
        print(M[i][::-1])
else:
    for i in range(1, N + 1):
        print(M[-i])
