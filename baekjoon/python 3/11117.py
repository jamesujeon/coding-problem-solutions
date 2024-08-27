# 문제 링크: https://www.acmicpc.net/problem/11117

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    b = [0] * 26
    for i in input().strip():
        b[ord(i) - 65] += 1

    for _ in range(int(input())):
        w = [0] * 26
        for i in input().strip():
            w[ord(i) - 65] += 1

        print('NO' if any(w[i] > b[i] for i in range(26)) else 'YES')
