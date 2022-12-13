# 문제 링크: https://www.acmicpc.net/problem/10214

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    counts = [0, 0]
    for _ in range(9):
        y, k = map(int, input().split())
        counts[0] += y
        counts[1] += k

    print("Yonsei" if counts[0] > counts[1] else "Korea")
