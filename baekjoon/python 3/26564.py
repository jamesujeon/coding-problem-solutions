# 문제 링크: https://www.acmicpc.net/problem/26564

for _ in range(int(input())):
    counts = {}
    for c in input().split():
        counts[c[0]] = counts.get(c[0], 0) + 1

    print(max(counts.values()))
