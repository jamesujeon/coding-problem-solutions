# 문제 링크: https://www.acmicpc.net/problem/20674

import sys
input = sys.stdin.readline

n, min_p = int(input()), int(input())
result = 0
for _ in range(1, n):
    p = int(input())
    if p > min_p:
        result += p - min_p
    else:
        min_p = p

print(result)
