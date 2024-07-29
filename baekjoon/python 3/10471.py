# 문제 링크: https://www.acmicpc.net/problem/10471

W, P = map(int, input().split())
L = [0] + list(map(int, input().split())) + [W]

print(*sorted(set(L[j] - L[i] for i in range(P + 2) for j in range(i + 1, P + 2))))
