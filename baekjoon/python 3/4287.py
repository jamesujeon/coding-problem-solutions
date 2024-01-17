# 문제 링크: https://www.acmicpc.net/problem/4287

import sys
input = sys.stdin.readline

while True:
    s = input().strip()
    if s == '#':
        break

    w = s.split()
    w.append(''.join(chr((ord(w[2][i]) + ord(w[1][i]) - ord(w[0][i]) - 97) % 26 + 97) for i in range(len(w[0]))))

    print(*w)
