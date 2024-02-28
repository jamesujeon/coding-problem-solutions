# 문제 링크: https://www.acmicpc.net/problem/5157

import sys
input = sys.stdin.readline

for k in range(1, int(input()) + 1):
    C, B, n, r = map(int, input().split())
    b = set(map(int, input().split()))

    a = 0
    for i in range(n):
        c, p = map(int, input().split())
        if c in b:
            a += p * r // 100

    print(f'Data Set {k}:\n{a}\n')
