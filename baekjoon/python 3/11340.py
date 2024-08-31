# 문제 링크: https://www.acmicpc.net/problem/11340

from math import ceil
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    p, t, m = map(int, input().split())
    f = ceil((9000 - p * 15 - t * 20 - m * 25) / 40)

    print(f if f < 101 else 'impossible')
