# 문제 링크: https://www.acmicpc.net/problem/7601

import sys
input = sys.stdin.readline

i = 1
while (s := input().strip()) != "0 0":
    n, d = map(int, s.split())
    r1, r2 = int(input()), int(input())

    print(f"Scenario {i}")
    for j in range(1, d + 1):
        c1, c2 = map(int, input().split())
        c1 += r1 and c1 >= r1
        c2 += r2 and c2 >= r2
        print(f"Day {j} {'OK' if c1 + c2 != n + 1 else 'ALERT'}")

    i += 1
