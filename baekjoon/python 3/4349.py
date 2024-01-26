# 문제 링크: https://www.acmicpc.net/problem/4349

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())

    s = set((i, j, N // i // j) for i in range(1, int(N**.5) + 1) for j in range(1, int((N // i)**.5) + 1) if N % (i * j) == 0)
    print(min((i * j + j * k + k * i) * 2 for i, j, k in s))
