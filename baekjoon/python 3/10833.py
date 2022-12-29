# 문제 링크: https://www.acmicpc.net/problem/10833

import sys
input = sys.stdin.readline

count = 0
for _ in range(int(input())):
    s, a = map(int, input().split())
    count += a % s

print(count)
