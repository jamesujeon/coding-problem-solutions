# 문제 링크: https://www.acmicpc.net/problem/5155

import sys
input = sys.stdin.readline

K = int(input())
for k in range(1, K + 1):
    n, m = map(int, input().split())

    mj = [0] * m
    m = [map(int, input().split()) for _ in range(m)]
    for _ in range(n):
        mj[int(input()) - 1] += 1

    print(f'Data Set {k}:')
    for i, (p, c, u, r) in enumerate(m):
        if p < (r - c) * min(mj[i], u):
            print(i + 1)
    print()
