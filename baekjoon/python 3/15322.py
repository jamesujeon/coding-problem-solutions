# 문제 링크: https://www.acmicpc.net/problem/15322

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    print((min(n, m) - 1) * 2)
