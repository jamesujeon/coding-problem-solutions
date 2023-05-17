# 문제 링크: https://www.acmicpc.net/problem/23103

import sys
input = sys.stdin.readline

p = [list(map(int, input().split())) for _ in range(int(input()))]

print(sum(abs(a - c) + abs(b - d) for (a, b), (c, d) in zip(p, p[1:])))
