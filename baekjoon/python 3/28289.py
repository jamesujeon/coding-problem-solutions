# 문제 링크: https://www.acmicpc.net/problem/28289

counts = [0] * 4
for _ in range(int(input())):
    G, C, _ = map(int, input().split())
    counts[(C > 2) + (C > 3) if G > 1 else 3] += 1

print(*counts, sep='\n')
