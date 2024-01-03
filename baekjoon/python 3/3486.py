# 문제 링크: https://www.acmicpc.net/problem/3486

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = input().split()

    print(int(str(int(a[::-1]) + int(b[::-1]))[::-1]))
