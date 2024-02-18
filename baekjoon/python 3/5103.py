# 문제 링크: https://www.acmicpc.net/problem/5103

import sys
input = sys.stdin.readline

while (C := input().strip()) != '#':
    M, S = map(int, input().split())
    for _ in range(int(input())):
        T, N = input().split()
        S = max(S - int(N), 0) if T == 'S' else min(S + int(N), M)

    print(C, S)
