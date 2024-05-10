# 문제 링크: https://www.acmicpc.net/problem/6965

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    print(' '.join("****" if len(w) == 4 else w for w in input().split()))
    print()
