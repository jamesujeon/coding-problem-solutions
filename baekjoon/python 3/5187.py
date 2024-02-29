# 문제 링크: https://www.acmicpc.net/problem/5187

import sys
input = sys.stdin.readline

for k in range(1, int(input()) + 1):
    m, n = map(int, input().split())
    g = [int(input()) for _ in range(m)]

    tw = 0
    for _ in range(n):
        h, w, d, i = map(int, input().split())
        tw += h * w * d * g[i - 1]

    print(f'Data Set {k}:\n{tw}')
