# 문제 링크: https://www.acmicpc.net/problem/25084

from math import pi
import sys
input = sys.stdin.readline

for i in range(1, int(input()) + 1):
    R, A, B = map(int, input().split())

    s = R**2
    while R > 0:
        s += (R * A)**2 + (R * A // B)**2
        R = R * A // B

    print(f"Case #{i}: {s * pi:.6f}")
