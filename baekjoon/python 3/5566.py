# 문제 링크: https://www.acmicpc.net/problem/5566

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
B = [int(input()) for _ in range(N)]
M = [int(input()) for _ in range(M)]

count = i = 0
for j in M:
    i = max(i + j + B[min(max(i + j, 0), N - 1)], 0)
    count += 1
    if i >= N:
        break

print(count)
