# 문제 링크: https://www.acmicpc.net/problem/13877

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k, s = input().split()
    print(k, '0' if '8' in s or '9' in s else int(s, 8), int(s), int(s, 16))
