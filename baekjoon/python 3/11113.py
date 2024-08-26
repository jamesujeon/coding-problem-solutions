# 문제 링크: https://www.acmicpc.net/problem/11113

import sys
input = sys.stdin.readline

n = [list(map(float, input().split())) for _ in range(int(input()))]
for _ in range(int(input())):
    _, p = input(), list(map(int, input().split()))

    d = 0
    for i in range(1, len(p)):
        d += ((n[p[i]][0] - n[p[i - 1]][0])**2 + (n[p[i]][1] - n[p[i - 1]][1])**2)**.5

    print(round(d))
