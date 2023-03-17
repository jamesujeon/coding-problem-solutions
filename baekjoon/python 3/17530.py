# 문제 링크: https://www.acmicpc.net/problem/17530

import sys
input = sys.stdin.readline

N, V = int(input()), int(input())
for _ in range(1, N):
    if int(input()) > V:
        print("N")
        break
else:
    print("S")
