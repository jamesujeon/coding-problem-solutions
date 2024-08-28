# 문제 링크: https://www.acmicpc.net/problem/11145

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().strip()
    if s.isdigit():
        print(int(s))
    else:
        print("invalid input")
