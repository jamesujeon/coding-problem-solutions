# 문제 링크: https://www.acmicpc.net/problem/6081

import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
H = [int(input()) for _ in range(N)]
for _ in range(Q):
    S, E = map(int, input().split())

    print(sum(H[S - 1:E]))
