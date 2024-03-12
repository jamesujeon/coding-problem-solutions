# 문제 링크: https://www.acmicpc.net/problem/5489

import sys
input = sys.stdin.readline

nums = {}
for _ in range(int(input())):
    x = int(input())
    nums[x] = nums.get(x, 0) + 1

print(sorted(nums.items(), key=lambda n: (-n[1], n[0]))[0][0])
