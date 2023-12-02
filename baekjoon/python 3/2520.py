# 문제 링크: https://www.acmicpc.net/problem/2520

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    input()
    cm, y, ssu, ssa, f = map(int, input().split())
    b, gs, gc, w = map(int, input().split())

    print(min(cm * 2, y * 2, ssu * 4, ssa * 16, f * 16 // 9, sum([b, gs // 30, gc // 25, w // 10])))
