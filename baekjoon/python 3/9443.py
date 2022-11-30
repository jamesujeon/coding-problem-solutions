# 문제 링크: https://www.acmicpc.net/problem/9443

import sys
input = sys.stdin.readline

indexes = set(ord(input()[0]) - 65 for _ in range(int(input())))

i = 0
while i in indexes:
    i += 1

print(i)
