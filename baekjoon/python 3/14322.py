# 문제 링크: https://www.acmicpc.net/problem/14322

import sys
input = sys.stdin.readline

for x in range(1, int(input()) + 1):
    y = [input().strip() for _ in range(int(input()))]
    y = sorted(y, key=lambda s: (-len(set(s.replace(' ', ''))), s))[0]

    print(f"Case #{x}: {y}")
