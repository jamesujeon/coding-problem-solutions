# 문제 링크: https://www.acmicpc.net/problem/13419

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().strip()
    s = s * (len(s) % 2 + 1)

    print(s[::2])
    print(s[1::2])
