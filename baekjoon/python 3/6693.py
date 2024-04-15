# 문제 링크: https://www.acmicpc.net/problem/6693

import sys
input = sys.stdin.readline

dl = 1 / 2**.5

while (s := input().strip()) != 'END':
    x = y = 0
    for d in s[:-1].split(','):
        i = sum(c.isdigit() for c in d)
        s, d = int(d[:i]), d[i:]
        if d == 'N':
            y += s
        elif d == 'NE':
            x += s * dl
            y += s * dl
        elif d == 'E':
            x += s
        elif d == 'SE':
            x += s * dl
            y -= s * dl
        elif d == 'S':
            y -= s
        elif d == 'SW':
            x -= s * dl
            y -= s * dl
        elif d == 'W':
            x -= s
        elif d == 'NW':
            x -= s * dl
            y += s * dl

    print(f'You can go to ({x:.3f},{y:.3f}), the distance is {(x**2 + y**2)**.5:.3f} steps.')
