# 문제 링크: https://www.acmicpc.net/problem/1874

import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]


stack, ops, index = [], [], 0
for i in range(1, n + 1):
    stack.append(i)
    ops.append('+')

    while stack and stack[-1] == nums[index]:
        stack.pop()
        ops.append('-')
        index += 1


print('\n'.join(ops) if not stack else 'NO')