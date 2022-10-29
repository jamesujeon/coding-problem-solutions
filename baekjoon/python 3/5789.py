# 문제 링크: https://www.acmicpc.net/problem/5789

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input()
    print('Do-it' if s[len(s) // 2 - 1] == s[len(s) // 2] else 'Do-it-Not')
