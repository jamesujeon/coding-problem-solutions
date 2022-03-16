# 문제 링크: https://www.acmicpc.net/problem/1247

import sys
input = sys.stdin.readline

results = [sum(int(input()) for _ in range(int(input()))) for _ in range(3)]
for result in results:
    print(('+' if result > 0 else '-') if result else 0)
