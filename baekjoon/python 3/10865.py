# 문제 링크: https://www.acmicpc.net/problem/10865

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

counts = [0] * N
for _ in range(M):
    A, B = map(int, input().split())

    counts[A - 1] += 1
    counts[B - 1] += 1

print('\n'.join(map(str, counts)))
