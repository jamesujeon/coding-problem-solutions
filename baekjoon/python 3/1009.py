# 문제 링크: https://www.acmicpc.net/problem/1009

import sys
input = sys.stdin.readline

cases = [map(int, input().split()) for _ in range(int(input()))]

for a, b in cases:
    print(((a % 10) ** (((b - 1) % 4) + 1)) % 10 if a % 10 else '10')
