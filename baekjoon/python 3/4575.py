# 문제 링크: https://www.acmicpc.net/problem/4575

import sys
input = sys.stdin.readline

while (s := input().strip()) != 'END':
    if len(set(s.replace(' ', ''))) == len(s.replace(' ', '')):
        print(s)
