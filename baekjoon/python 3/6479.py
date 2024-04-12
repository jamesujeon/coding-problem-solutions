# 문제 링크: https://www.acmicpc.net/problem/6479

import sys
input = sys.stdin.readline

while (n := int(input())) != 0:
    input()

    f = 1
    for i in range(2, n + 1):
        f *= i
    f = str(f)

    print(f'{n}! --')
    for i in range(10):
        print(f'   ({i}){f.count(str(i)):>5}', end=' ')
        if i == 4 or i == 9:
            print()
