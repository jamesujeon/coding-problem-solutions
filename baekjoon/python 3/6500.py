# 문제 링크: https://www.acmicpc.net/problem/6500

import sys
input = sys.stdin.readline

while (a := int(input())) != 0:
    r = set()
    while a not in r:
        r.add(a)
        a = (a * a) % 1000000 // 100

    print(len(r))
