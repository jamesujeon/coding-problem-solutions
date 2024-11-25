# 문제 링크: https://www.acmicpc.net/problem/14758

import sys
input = sys.stdin.readline

while (s := input().strip()) != '0 0 0 0 0 0':
    n, w, l, h, a, m = map(int, s.split())
    c = w * l + (w + l) * h * 2
    for _ in range(m):
        mw, mh = map(int, input().split())
        c -= mw * mh

    print((c * n + a - 1) // a)
