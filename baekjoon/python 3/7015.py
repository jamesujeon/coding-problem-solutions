# 문제 링크: https://www.acmicpc.net/problem/7015

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    y, m, d = map(int, input().split())

    d += (y - 1) * 195 + (y - 1) // 3 * 5
    d += (m - 1) * 20 - ((m - 1) // 2 if y % 3 else 0)

    print(196471 - d)
