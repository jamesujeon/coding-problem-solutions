# 문제 링크: https://www.acmicpc.net/problem/9954

import sys
input = sys.stdin.readline

while (t := input().strip()) != '#':
    s = ord(t[-1]) - 65

    def f(c):
        b = 65 if c.isupper() else 97
        return chr((ord(c) - b - s) % 26 + b) if c.isalpha() else c

    print(''.join(map(f, t[:-1])))
