# 문제 링크: https://www.acmicpc.net/problem/9070

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    p = []
    for _ in range(int(input())):
        W, C = map(int, input().split())
        p.append((C / W, C))

    print(sorted(p)[0][1])
