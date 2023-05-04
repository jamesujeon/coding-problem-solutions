# 문제 링크: https://www.acmicpc.net/problem/22093

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, a, b = map(int, input().split())

    print(max(a - b, 0), min(a, n - b))
