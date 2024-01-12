# 문제 링크: https://www.acmicpc.net/problem/4117

import sys
input = sys.stdin.readline

while True:
    N, T1, T2, T3 = map(int, input().split())
    if N == T1 == T2 == T3 == 0:
        break

    print(N * 4 - 1 + (T2 - T1) % N + (T2 - T3) % N)
