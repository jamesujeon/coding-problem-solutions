# 문제 링크: https://www.acmicpc.net/problem/4176

import sys
input = sys.stdin.readline

while True:
    s = input().strip()
    if s == 'END':
        break

    i = 1
    while s != (x := str(len(s))):
        s = x
        i += 1

    print(i)
