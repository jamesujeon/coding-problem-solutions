# 문제 링크: https://www.acmicpc.net/problem/15917

import sys
input = sys.stdin.readline

a = set(2**i for i in range(31))

for _ in range(int(input())):
    print(int(int(input()) in a))
