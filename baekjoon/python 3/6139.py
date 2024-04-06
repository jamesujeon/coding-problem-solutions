# 문제 링크: https://www.acmicpc.net/problem/6139

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
for _ in range(K):
    S, T, R = map(int, input().split())
    S = (N + S - 1) // S
    print(S + (S - 1) // T * R)
