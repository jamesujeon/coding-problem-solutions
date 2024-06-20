# 문제 링크: https://www.acmicpc.net/problem/9377

import sys
input = sys.stdin.readline

while (n := int(input())) != 0:
    w = [input().strip() for _ in range(n)]

    i = -1
    while len(set(w)) == n and '' not in w:
        w = [s[1:] for s in w]
        i += 1

    print(max(i, 0))
