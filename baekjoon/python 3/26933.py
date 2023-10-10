# 문제 링크: https://www.acmicpc.net/problem/26933

cost = 0
for _ in range(int(input())):
    H, B, K = map(int, input().split())
    cost += max(B - H, 0) * K

print(cost)
