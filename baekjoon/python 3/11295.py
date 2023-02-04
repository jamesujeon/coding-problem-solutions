# 문제 링크: https://www.acmicpc.net/problem/11295

import sys
input = sys.stdin.readline

U = 0
while True:
    L = int(input())
    if L == 0:
        break

    U +=1
    print(f"User {U}")
    for _ in range(int(input())):
        print(f"{int(input()) * L / 100000:.5f}")
