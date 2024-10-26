# 문제 링크: https://www.acmicpc.net/problem/14041

h, m = map(int, input().split(':'))

t = h * 60 + m
for _ in range(12):
    t = (t + (1 + (420 <= t < 600 or 900 <= t < 1140)) * 10) % 1440

print(f"{t // 60:02d}:{t % 60:02d}")
