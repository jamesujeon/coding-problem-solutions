# 문제 링크: https://www.acmicpc.net/problem/22388

import sys
input = sys.stdin.readline

while True:
    try:
        y, m, d = map(int, input().split()[1:])
    except:
        break

    g = "HEISEI"
    if y * 10000 + m * 100 + d > 310430:
        g = '?'
        y -= 30

    print(g, y, m, d)
