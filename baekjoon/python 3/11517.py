# 문제 링크: https://www.acmicpc.net/problem/11517

import sys
input = sys.stdin.readline

while (s := input().strip()) != '-1 -1 -1 -1':
    s = list(map(int, s.split()))
    d, r = (s[1] - s[0], s[1] / s[0]) if s.index(-1) > 1 else (s[3] - s[2], s[3] / s[2])
    if r != int(r):
        r = -1

    o = -1
    if s[0] < 0:
        if s[1] + d == s[2]:
            o = s[1] - d
        elif s[1] * r == s[2]:
            o = s[1] / r
    elif s[1] < 0:
        if s[0] + d * 2 == s[2]:
            o = s[0] + d
        elif s[0] * r * r == s[2]:
            o = s[0] * r
    elif s[2] < 0:
        if s[1] + d * 2 == s[3]:
            o = s[1] + d
        elif s[1] * r * r == s[3]:
            o = s[1] * r
    else:
        if s[1] + d == s[2]:
            o = s[2] + d
        elif s[1] * r == s[2]:
            o = s[2] * r

    if o < 1 or o > 10000 or o != int(o):
        o = -1

    print(int(o))
