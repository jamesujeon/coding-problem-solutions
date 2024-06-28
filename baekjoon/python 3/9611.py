# 문제 링크: https://www.acmicpc.net/problem/9611

import sys
input = sys.stdin.readline

p = [list(map(int, input().split())) for _ in range(int(input()))]

for _ in range(int(input())):
    i, d = map(int, input().split())
    xi, yi = p[i - 1]

    print(sum((xi - xj)**2 + (yi - yj)**2 <= d * d for xj, yj in p[:i - 1] + p[i:]))
