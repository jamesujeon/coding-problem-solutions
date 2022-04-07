# 문제 링크: https://www.acmicpc.net/problem/2720

import sys
input = sys.stdin.readline

results = []
for _ in range(int(input())):
    cent = int(input())

    moneys = [0] * 4
    moneys[0], cent = cent // 25, cent % 25
    moneys[1], cent = cent // 10, cent % 10
    moneys[2], cent = cent // 5, cent % 5
    moneys[3] = cent

    results.append(' '.join(map(str, moneys)))

for result in results:
    print(result)
