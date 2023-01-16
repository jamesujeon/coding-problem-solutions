# 문제 링크: https://www.acmicpc.net/problem/11161

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    count = P = 0
    for _ in range(int(input())):
        P1, P2 = map(int, input().split())
        P += P1 - P2
        count = min(count, P)
    count *= -1

    print(count)
