# 문제 링크: https://www.acmicpc.net/problem/7523

import sys
input = sys.stdin.readline

for i in range(1, int(input()) + 1):
    n, m = map(int, input().split())

    print(f"Scenario #{i}:")
    print((m * (m + 1) - n * (n - 1)) // 2)
    print()
