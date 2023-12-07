# 문제 링크: https://www.acmicpc.net/problem/2703

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s, c = input().strip(), input().strip()
    print(''.join(c[ord(ch) - 65] if ch.isupper() else ch for ch in s))
