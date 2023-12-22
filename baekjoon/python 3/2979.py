# 문제 링크: https://www.acmicpc.net/problem/2979

costs = list(map(int, input().split()))
counts = [0] * 100
for _ in range(3):
    i, j = map(int, input().split())
    for k in range(i, j):
        counts[k] += 1

print(sum(costs[i - 1] * counts.count(i) * i for i in range(1, 4)))
