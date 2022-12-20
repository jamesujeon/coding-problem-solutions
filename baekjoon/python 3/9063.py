# 문제 링크: https://www.acmicpc.net/problem/9063

import sys
input = sys.stdin.readline

n = int(input())
min_x, min_y = map(int, input().split())
max_x, max_y = min_x, min_y

for _ in range(n - 1):
    x, y = map(int, input().split())
    min_x = min(x, min_x)
    min_y = min(y, min_y)
    max_x = max(x, max_x)
    max_y = max(y, max_y)

print((max_x - min_x) * (max_y - min_y))
