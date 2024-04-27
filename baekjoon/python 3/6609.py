# 문제 링크: https://www.acmicpc.net/problem/6609

import sys
input = sys.stdin.readline

while True:
    try:
        M, P, L, E, R, S, N = map(int, input().split())
    except:
        break

    for _ in range(N):
        M, P, L = P // S, L // R, M * E

    print(M)
