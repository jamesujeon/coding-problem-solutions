# 문제 링크: https://www.acmicpc.net/problem/22279

import sys
input = sys.stdin.readline

qaly = 0
for _ in range(int(input())):
    q, y = map(float, input().split())
    qaly += q * y

print(qaly)
