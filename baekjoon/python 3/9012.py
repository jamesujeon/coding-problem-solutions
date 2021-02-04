# 문제 링크: https://www.acmicpc.net/problem/9012

import sys
input = sys.stdin.readline

def is_vps(s: str) -> bool:
    stack = 0
    for ch in s:
        stack += 1 if ch == '(' else -1
        if stack < 0:
            break
    return stack == 0

for _ in range(int(input())):
    print('YES' if is_vps(input().strip()) else 'NO')