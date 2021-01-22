# 문제 링크: https://www.acmicpc.net/problem/1002

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = (abs(x1 - x2)**2 + abs(y1 - y2)**2)**.5
    r_sum = r1 + r2
    r_dist = abs(r1 - r2)

    if dist == 0:
        print(-1 if r_dist == 0 else 0)
    elif dist > r_sum:
        print(0)
    elif dist == r_sum:
        print(1)
    elif dist > r_dist:
        print(2)
    elif dist == r_dist:
        print(1)
    else:
        print(0)