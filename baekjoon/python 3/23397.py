# 문제 링크: https://www.acmicpc.net/problem/23397

import sys
input = sys.stdin.readline

T, D, M = map(int, input().split())
Y = [0] + [int(input()) for _ in range(M)] + [D]

print("Y" if T <= max(y2 - y1 for y1, y2 in zip(Y, Y[1:])) else "N")
