# 문제 링크: https://www.acmicpc.net/problem/22396

from math import ceil
import sys
input = sys.stdin.readline

while True:
    R0, W0, C, R = map(int, input().split())
    if R0 == W0 == C == R == 0:
        break

    if R0 / W0 < C:
        print(ceil((C * W0 - R0) / R))
    else:
        print(0)
