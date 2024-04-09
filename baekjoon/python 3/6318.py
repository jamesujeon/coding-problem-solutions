# 문제 링크: https://www.acmicpc.net/problem/6318

import sys
input = sys.stdin.readline

i = 1
while (n := int(input())) != 0:
    b = list(map(int, input().split()))
    h = sum(b) // n

    print(f'Set #{i}\nThe minimum number of moves is {sum(max(i - h, 0) for i in b)}.\n')
    i += 1
