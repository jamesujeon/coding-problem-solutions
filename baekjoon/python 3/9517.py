# 문제 링크: https://www.acmicpc.net/problem/9517

import sys
input = sys.stdin.readline

B, K = 210, int(input())
for _ in range(int(input())):
    T, Z = input().split()

    B -= int(T)
    if B <= 0:
        print(K)
        break

    if Z == 'T':
        K = K + 1 if K < 8 else 1
