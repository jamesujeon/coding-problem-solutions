# 문제 링크: https://www.acmicpc.net/problem/13163

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    print(f"god{''.join(input().split()[1:])}")
