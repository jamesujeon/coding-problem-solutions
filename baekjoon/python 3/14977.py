# 문제 링크: https://www.acmicpc.net/problem/14977

import sys
input = sys.stdin.readline


def f():
    n = int(input())
    x = list(map(int, input().split()))
    if n == 1:
        print(1)
        return

    d = x[-1] - x[-2]
    i = n - 1
    while i > 1 and x[i - 1] - x[i - 2] == d:
        i -= 1
    print(i)


while True:
    try:
        f()
    except:
        break
