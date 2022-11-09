# 문제 링크: https://www.acmicpc.net/problem/8574

import sys
input = sys.stdin.readline

n, k, x, y = map(int, input().split())

count = 0
for _ in range(n):
    xi, yi = map(int, input().split())
    if (xi - x)**2 + (yi - y)**2 > k**2:
        count += 1

print(count)
