# 문제 링크: https://www.acmicpc.net/problem/4562

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    X, Y = map(int, input().split())
    print('MMM BRAINS' if X >= Y else 'NO BRAINS')
