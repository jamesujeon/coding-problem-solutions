# 문제 링크: https://www.acmicpc.net/problem/17588

import sys
input = sys.stdin.readline

nums = [int(input()) for _ in range(int(input()))]

if len(nums) == nums[-1]:
    print("good job")
else:
    for num in sorted(set(range(1, nums[-1] + 1)) - set(nums)):
        print(num)
