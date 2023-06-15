# 문제 링크: https://www.acmicpc.net/problem/24408

import sys
input = sys.stdin.readline

i = 0
for _ in range(int(input())):
    num = int(input())
    if not i:
        i = num
    elif num % i == 0:
        print(num)
        i = 0
