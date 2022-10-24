# 문제 링크: https://www.acmicpc.net/problem/7782

import sys
input = sys.stdin.readline

n = int(input())
b1, b2 = map(int, input().split())
for _ in range(n):
    lx, ly, hx, hy = map(int, input().split())
    if lx <= b1 <= hx and ly <= b2 <= hy:
        print('Yes')
        break
else:
    print('No')
