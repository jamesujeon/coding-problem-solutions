# 문제 링크: https://www.acmicpc.net/problem/2711

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    i, s = input().split()
    print(s[:int(i) - 1] + s[int(i):])
