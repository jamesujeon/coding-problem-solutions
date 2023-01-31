# 문제 링크: https://www.acmicpc.net/problem/10419

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    d = int(input())

    t = int(d**.5)
    while t * (t + 1) > d:
        t -= 1

    print(t)
