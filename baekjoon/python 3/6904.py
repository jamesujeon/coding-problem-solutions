# 문제 링크: https://www.acmicpc.net/problem/6904

import sys
input = sys.stdin.readline

while (C := int(input())) != 0:
    d = int(C**.5)
    while C % d:
        d -= 1

    print(f"Minimum perimeter is {(d + C // d) * 2} with dimensions {d} x {C // d}")
