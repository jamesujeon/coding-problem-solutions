# 문제 링크: https://www.acmicpc.net/problem/7947

import sys
input = sys.stdin.readline
avg = lambda x: int(x / 10 + .5)

for _ in range(int(input())):
    r = g = b = 0
    for _ in range(10):
        rgb = list(map(int, input().split()))
        r += rgb[0]
        g += rgb[1]
        b += rgb[2]

    print(avg(r), avg(g), avg(b))
