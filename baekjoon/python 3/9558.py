# 문제 링크: https://www.acmicpc.net/problem/9558

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a1 = sorted(set(map(int, input().split()[1:])))
    a2 = sorted(set(map(int, input().split()[1:])))

    m, i, j = abs(a1[0] - a2[0]), 0, 0
    while i < len(a1) and j < len(a2):
        m = min(abs(a1[i] - a2[j]), m)
        if a1[i] < a2[j]:
            i += 1
        else:
            j += 1

    print(m)
