# 문제 링크: https://www.acmicpc.net/problem/9295

import sys
input = sys.stdin.readline

for i in range(1, int(input()) + 1):
    print(f"Case {i}: {sum(map(int, input().split()))}")
