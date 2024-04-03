# 문제 링크: https://www.acmicpc.net/problem/6014

import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
B = []
for i in range(N):
    B += [i + 1] * int(input())

print('\n'.join(str(B[int(input())]) for _ in range(Q)))
