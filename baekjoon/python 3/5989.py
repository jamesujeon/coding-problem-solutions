# 문제 링크: https://www.acmicpc.net/problem/5989

import sys
input = sys.stdin.readline

X, Y, I = map(int, input().split())

F = [[0] * Y for _ in range(X)]
for _ in range(I):
    Xll, Yll, Xur, Yur = map(int, input().split())

    for i in range(Xll - 1, Xur):
        for j in range(Yll - 1, Yur):
            F[i][j] = 1

print(sum(sum(F[i]) for i in range(X)))
