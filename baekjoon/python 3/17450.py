# 문제 링크: https://www.acmicpc.net/problem/17450

ratios = []
for i in range(3):
    p, w = map(int, input().split())
    if p >= 500:
        p -= 50

    ratios.append(w / p)

print("SNU"[ratios.index(max(ratios))])
