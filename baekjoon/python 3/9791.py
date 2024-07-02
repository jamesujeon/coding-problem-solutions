# 문제 링크: https://www.acmicpc.net/problem/9791

import sys
input = sys.stdin.readline

while (b := input().strip()) != '0':
    d, i = '', 0
    for j in range(len(b)):
        if b[i] != b[j]:
            d += f"{j - i}{b[i]}"
            i = j
    d += f"{len(b) - i}{b[i]}"

    print(d)
