# 문제 링크: https://www.acmicpc.net/problem/13064

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().strip()
    if all(c in '123456789' for c in s[:4] + s[5:]) and s[0] == s[1] and s[4].isupper():
        print(s)
