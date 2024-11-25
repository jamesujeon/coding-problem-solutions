# 문제 링크: https://www.acmicpc.net/problem/14771

import sys
input = sys.stdin.readline

for x in range(1, int(input()) + 1):
    n, v = map(int, input().split())
    n = [list(map(int, input().split())) for _ in range(n)]

    p = 0
    for _ in range(v):
        a1, a2, c = map(int, input().split())
        p += n[a1 - 1][0] * n[a1 - 1][1] + n[a2 - 1][0] * n[a2 - 1][1]
        if c > 0:
            a = a1 if c == 1 else a2
            p += (not n[a - 1][0]) * n[a - 1][1]

    print(f"Data Set {x}:\n{p}\n")
