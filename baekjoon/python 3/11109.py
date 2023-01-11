# 문제 링크: https://www.acmicpc.net/problem/11109

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    d, n, s, p = map(int, input().split())

    s *= n
    p = d + n * p

    if s > p:
        print("parallelize")
    elif s < p:
        print("do not parallelize")
    else:
        print("does not matter")
