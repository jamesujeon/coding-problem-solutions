# 문제 링크: https://www.acmicpc.net/problem/7510

import sys
input = sys.stdin.readline

for i in range(int(input())):
    a, b, c = sorted(map(int, input().split()))

    print(f"Scenario #{i + 1}:")
    print(f"{'yes' if a**2 + b**2 == c**2 else 'no'}\n")
