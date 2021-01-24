# 문제 링크: https://www.acmicpc.net/problem/1181

import sys
input = sys.stdin.readline

for word in sorted(list(set(input().strip() for _ in range(int(input())))), key=lambda s: (len(s), s)):
    print(word)