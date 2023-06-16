# 문제 링크: https://www.acmicpc.net/problem/24569

import sys
input = sys.stdin.readline

N = int(input())
count = 0
for _ in range(N):
    if int(input()) * 5 - int(input()) * 3 > 40:
        count += 1

print(f"{count}{'+' if count == N else ''}")
