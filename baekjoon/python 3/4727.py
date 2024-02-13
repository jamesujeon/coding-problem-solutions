# 문제 링크: https://www.acmicpc.net/problem/4727

import sys
input = sys.stdin.readline

while (s := input().strip()) != '0 0 0 0':
    c, gf, gc, gp = map(int, s.split())

    min_c = int(max(gf - .5, 0) * 9 + max(gc - .5, 0) * 4 + max(gp - .5, 0) * 4 + .5)
    max_c = int((gf + .5) * 9 + (gc + .5) * 4 + (gp + .5) * 4 + .5)
    print('yes' if min_c <= c < max_c else 'no')
