# 문제 링크: https://www.acmicpc.net/problem/6696

from math import ceil, pi
import sys
input = sys.stdin.readline

while (s := input().strip()) != '0 0':
    x, y = map(float, s.split())

    print(f'The property will be flooded in hour {ceil((x * x + y * y) * pi / 100)}.')
