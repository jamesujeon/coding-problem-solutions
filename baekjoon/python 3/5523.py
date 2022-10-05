# 문제 링크: https://www.acmicpc.net/problem/5523

import sys
input = sys.stdin.readline

counts = [0, 0]
for _ in range(int(input())):
    A, B = map(int, input().split())

    if A != B:
        counts[A < B] += 1

print(counts[0], counts[1])
