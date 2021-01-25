# 문제 링크: https://www.acmicpc.net/problem/10773

import sys
input = sys.stdin.readline

stack = []
for _ in range(int(input())):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))