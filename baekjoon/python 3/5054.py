# 문제 링크: https://www.acmicpc.net/problem/5054

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    _, x = input(), list(map(int, input().split()))

    print((max(x) - min(x)) * 2)
