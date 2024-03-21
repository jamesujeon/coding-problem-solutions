# 문제 링크: https://www.acmicpc.net/problem/5742

import sys
input = sys.stdin.readline

while (s := input().strip()) != '0 0 0':
    N, C, K = map(int, s.split())

    K = [0] * K
    for _ in range(N):
        for X in map(int, input().split()):
            K[X - 1] += 1
    min_K = min(K)

    print(*(i + 1 for i in range(len(K)) if K[i] == min_K))
