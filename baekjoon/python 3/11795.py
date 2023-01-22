# 문제 링크: https://www.acmicpc.net/problem/11795

import sys
input = sys.stdin.readline

sets = [0, 0, 0]
for _ in range(int(input())):
    new_sets = list(map(int, input().split()))
    for i in range(3):
        sets[i] += new_sets[i]

    min_set = min(sets)
    if min_set < 30:
        print("NO")
        continue

    print(min_set)
    for i in range(3):
        sets[i] -= min_set
