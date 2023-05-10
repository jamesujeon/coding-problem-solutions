# 문제 링크: https://www.acmicpc.net/problem/22380

import sys
input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    if N == M == 0:
        break

    print(sum(min(A, M // N) for A in map(int, input().split())))
