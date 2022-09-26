# 문제 링크: https://www.acmicpc.net/problem/4504

import sys

n = int(input())
nums = map(int, sys.stdin.read().split())

for num in nums:
    if num == 0:
        break
    print(f"{num} is {'NOT ' if num % n else ''}a multiple of {n}.")
