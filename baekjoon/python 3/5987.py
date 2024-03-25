# 문제 링크: https://www.acmicpc.net/problem/5987

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, C, S = input().split()
    for _ in range(int(C)):
        S = S[int(N):] + S

    print(S)
