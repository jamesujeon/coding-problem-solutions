# 문제 링크: https://www.acmicpc.net/problem/2858

R, B = map(int, input().split())

for W in range(3, R // 2):
    L = (R + 4) // 2 - W
    if L * W == R + B:
        print(L, W)
        break
