# 문제 링크: https://www.acmicpc.net/problem/1654

import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]


def count_lines(base):
    return sum(l // base for l in lines if l >= base)

max_line = 1
low, high = 1, sum(lines) // N
while low <= high:
    mid = (low + high) // 2
    if count_lines(mid) >= N:
        max_line = mid
        low = mid + 1
    else:
        high = mid - 1


print(max_line)