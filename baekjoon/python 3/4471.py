# 문제 링크: https://www.acmicpc.net/problem/4471

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s1 = input().strip()
    x1, y1, z1 = map(float, input().split())
    s2 = input().strip()
    x2, y2, z2 = map(float, input().split())

    print(f'{s1} to {s2}: {((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)**.5:.2f}')
