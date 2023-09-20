# 문제 링크: https://www.acmicpc.net/problem/27194

from math import ceil

n, T = map(int, input().split())
m = int(input())
x, y = map(int, input().split())

print(max(ceil((m / x + (n - m) / y) / 60 - T), 0))
