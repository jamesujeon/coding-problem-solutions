# 문제 링크: https://www.acmicpc.net/problem/16175

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())

    votes = [0] * N
    for _ in range(M):
        for i, v in enumerate(map(int, input().split())):
            votes[i] += v

    print(votes.index(max(votes)) + 1)
