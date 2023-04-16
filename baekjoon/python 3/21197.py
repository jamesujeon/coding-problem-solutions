# 문제 링크: https://www.acmicpc.net/problem/21197

import sys
input = sys.stdin.readline

N = int(input())
if N % 2 == 0:
    t = [int(input()) for _ in range(N)]
    print(sum(t[i + 1] - t[i] for i in range(0, N, 2)))
else:
    print("still running")
