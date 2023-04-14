# 문제 링크: https://www.acmicpc.net/problem/21105

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    P, C = map(float, input().split())
    print(P / (C + 100) * 100)
