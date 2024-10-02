# 문제 링크: https://www.acmicpc.net/problem/12836

import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
b = [0] * N
for _ in range(Q):
    i, j, k = map(int, input().split())
    if i == 1:
        b[j - 1] += k
    else:
        print(sum(b[j - 1:k]))
