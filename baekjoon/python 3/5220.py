# 문제 링크: https://www.acmicpc.net/problem/5220

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, c = map(int, input().split())

    print("Valid" if bin(n).count('1') % 2 == c else "Corrupt")
