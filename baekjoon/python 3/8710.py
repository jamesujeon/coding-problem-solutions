# 문제 링크: https://www.acmicpc.net/problem/8710

from math import ceil

k, w, m = map(int, input().split())

print(ceil((w - k) / m))
