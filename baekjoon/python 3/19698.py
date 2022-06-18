# 문제 링크: https://www.acmicpc.net/problem/19698

N, W, H, L = map(int, input().split())

print(min((W // L) * (H // L), N))
