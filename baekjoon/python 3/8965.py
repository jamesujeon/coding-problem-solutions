# 문제 링크: https://www.acmicpc.net/problem/8965

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().strip()

    print(sorted(s[i:] + s[:i] for i in range(len(s)))[0])
