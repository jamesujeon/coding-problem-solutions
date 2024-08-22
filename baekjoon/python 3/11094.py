# 문제 링크: https://www.acmicpc.net/problem/11094

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().strip()
    if s.startswith("Simon says"):
        print(s[10:])
