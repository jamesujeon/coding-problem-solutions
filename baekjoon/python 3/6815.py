# 문제 링크: https://www.acmicpc.net/problem/6815

from math import ceil, floor, cbrt

print(sum((i**1.5) % 1 == 0 for i in range(ceil(cbrt(int(input()))), floor(cbrt(int(input()))) + 1)))
