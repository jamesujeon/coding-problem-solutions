# 문제 링크: https://www.acmicpc.net/problem/4697

from math import ceil

while (s := input()) != '0 0 0 0 0 0':
    n, w, l, h, a, m = map(int, s.split())
    ma = 0
    for _ in range(m):
        mw, mh = map(int, input().split())
        ma += mw * mh

    print(ceil((w * l + (l * h + h * w) * 2 - ma) * n / a))
