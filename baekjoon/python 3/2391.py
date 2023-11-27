# 문제 링크: https://www.acmicpc.net/problem/2391

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().strip()
    min_w = (s, len(s) + 1)
    for _ in range(int(input())):
        w = input().strip()
        d = sum(s[i] != w[i] for i in range(len(s)))
        if d < min_w[1]:
            min_w = (w, d)

    print(min_w[0])
