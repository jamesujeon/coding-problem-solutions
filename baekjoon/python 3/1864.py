# 문제 링크: https://www.acmicpc.net/problem/1864

import sys
input = sys.stdin.readline

n = "-\\(@?>&%"

while True:
    s = input().strip()[::-1]
    if s == '#':
        break

    print(sum((n.find(s[i])) * 8**i for i in range(len(s))))
