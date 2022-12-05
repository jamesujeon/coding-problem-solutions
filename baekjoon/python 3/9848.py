# 문제 링크: https://www.acmicpc.net/problem/9848

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
count, prev_t = 0, int(input())
for i in range(n - 1):
    t = int(input())
    if t + k <= prev_t:
        count += 1
    prev_t = t

print(count)
