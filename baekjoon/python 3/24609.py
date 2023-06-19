# 문제 링크: https://www.acmicpc.net/problem/24609

import sys
input = sys.stdin.readline

result = balance = 0
for _ in range(int(input())):
    balance += int(input())
    if balance < result:
        result = balance

print(-result)
