# 문제 링크: https://www.acmicpc.net/problem/25756

input()

V = 0
for A in map(int, input().split()):
    V = 1 - (1 - V) * (1 - A / 100)

    print(f"{V * 100:.6f}")
