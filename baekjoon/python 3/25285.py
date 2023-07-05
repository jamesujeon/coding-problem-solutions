# 문제 링크: https://www.acmicpc.net/problem/25285

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    h, w = map(int, input().split())

    if h < 159 or h >= 204:
        if h < 141:
            print(6)
        elif h < 146:
            print(5)
        else:
            print(4)
        continue

    bmi = w / (h / 100)**2
    if h < 161:
        if bmi < 16 or bmi >= 35:
            print(4)
        else:
            print(3)
    else:
        if bmi < 16 or bmi >= 35:
            print(4)
        elif 16 <= bmi < 18.5 or 30 <= bmi < 35:
            print(3)
        elif 18.5 <= bmi < 20 or 25 <= bmi < 30:
            print(2)
        else:
            print(1)
