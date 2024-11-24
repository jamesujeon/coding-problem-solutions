# 문제 링크: https://www.acmicpc.net/problem/14726

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = list(map(int, input().strip()))
    print('FT'[sum(n[i] if i % 2 else sum(map(int, str(n[i] * 2))) for i in range(16)) % 10 == 0])
