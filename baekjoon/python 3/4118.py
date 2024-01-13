# 문제 링크: https://www.acmicpc.net/problem/4118

import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if N == 0:
        break

    nums = set()
    for _ in range(N):
        nums |= set(map(int, input().split()))

    print('Yes' if len(nums) == 49 else 'No')
