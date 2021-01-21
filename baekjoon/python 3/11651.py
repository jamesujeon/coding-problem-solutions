# 문제 링크: https://www.acmicpc.net/problem/11651

coords = [tuple(map(int, input().split())) for _ in range(int(input()))]

for y, x in sorted(coords, key=lambda c: (c[1], c[0])):
    print(y, x)