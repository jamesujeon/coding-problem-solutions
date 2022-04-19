# 문제 링크: https://www.acmicpc.net/problem/5532

from math import ceil

l, a, b, c, d = (int(input()) for _ in range(5))

print(l - max(ceil(a / c), ceil(b / d)))
