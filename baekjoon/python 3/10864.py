# 문제 링크: https://www.acmicpc.net/problem/10864

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N = [0] * N
for _ in range(M):
    A, B = map(int, input().split())
    N[A - 1] += 1
    N[B - 1] += 1

print(*N, sep='\n')
