# 문제 링크: https://www.acmicpc.net/problem/3034

n, w, h = map(int, input().split())

max_dist = int((w * w + h * h) ** .5)
for _ in range(n):
    print('DA' if int(input()) <= max_dist else 'NE')