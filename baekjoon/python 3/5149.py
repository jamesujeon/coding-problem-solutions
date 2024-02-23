# 문제 링크: https://www.acmicpc.net/problem/5149

import sys
input = sys.stdin.readline

for k in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    p = [list(map(int, input().split())) for _ in range(n)]
    s = list(map(int, input().split()))

    lp = rp = p[s[0] - 1]
    for i in s[1:]:
        x, y = p[i - 1]
        lp = [min(x, lp[0]), min(y, lp[1])]
        rp = [max(x, rp[0]), max(y, rp[1])]

    print(f'Data Set {k}:\n{sum(lp[0] <= x <= rp[0] and lp[1] <= y <= rp[1] for x, y in p)}\n')
