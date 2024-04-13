# 문제 링크: https://www.acmicpc.net/problem/6693

import sys
input = sys.stdin.readline

while (s := input().strip()) != '0+0=0':
    s, c = s.split('=')
    a, b = s.split('+')
    print(int(a[::-1]) + int(b[::-1]) == int(c[::-1]))

print(True)
