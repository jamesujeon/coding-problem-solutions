# 문제 링크: https://www.acmicpc.net/problem/16427

from math import ceil

_, s = map(int, input().split())
print(ceil(max(map(int, input().split())) * s / 1000))
