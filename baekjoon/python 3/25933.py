# 문제 링크: https://www.acmicpc.net/problem/25933

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    g1, s1, b1, g2, s2, b2 = map(int, input().split())

    result = "none"
    if g1 + s1 + b1 > g2 + s2 + b2:
        result = "count"
    if g1 > g2 or (g1 == g2 and s1 > s2) or (g1 == g2 and s1 == s2 and b1 > b2):
        if result == "count":
            result = "both"
        else:
            result = "color"

    print(g1, s1, b1, g2, s2, b2)
    print(result)
    print()
