# 문제 링크: https://www.acmicpc.net/problem/5145

import sys
input = sys.stdin.readline

for k in range(1, int(input()) + 1):
    n = int(input())
    p = [int(input()) for _ in range(n - 1)]
    s = [input() for _ in range(n)]
    s_s, e_s = (input() for _ in range(2))

    print(f'Data Set {k}:\n{p[abs(s.index(s_s) - s.index(e_s)) - 1]}\n')
