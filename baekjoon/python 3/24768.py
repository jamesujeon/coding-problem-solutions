# 문제 링크: https://www.acmicpc.net/problem/24768

import sys
input = sys.stdin.readline

while True:
    x, y = map(int, input().split())
    if x == y == 0:
        break

    if x + y == 13:
        print("Never speak again.")
    elif x > y:
        print("To the convention.")
    elif x == y:
        print("Undecided.")
    else:
        print("Left beehind.")
