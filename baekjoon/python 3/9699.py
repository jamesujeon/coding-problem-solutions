# 문제 링크: https://www.acmicpc.net/problem/9699

import sys
input = sys.stdin.readline

for i in range(1, int(input()) + 1):
    print(f"Case #{i}: {max(map(int, input().split()))}")
