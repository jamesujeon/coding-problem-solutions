# 문제 링크: https://www.acmicpc.net/problem/5235

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    nums = list(map(int, input().split()))[1:]

    evens = odds = 0
    for num in nums:
        if num % 2:
            odds += num
        else:
            evens += num

    if evens > odds:
        print("EVEN")
    elif evens < odds:
        print("ODD")
    else:
        print("TIE")
