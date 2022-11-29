# 문제 링크: https://www.acmicpc.net/problem/9288

import sys
input = sys.stdin.readline

for i in range(1, int(input()) + 1):
    n = int(input())

    print(f"Case {i}:")
    for j in range(max(1, n - 6), min(7, n // 2 + 1)):
        print(f"({j},{n - j})")
