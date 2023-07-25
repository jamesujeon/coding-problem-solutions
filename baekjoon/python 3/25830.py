# 문제 링크: https://www.acmicpc.net/problem/25830

m, s = map(int, input().split(':'))

t = m * 3540 + s * 59

print(f"{t // 3600:02d}:{t // 60 % 60:02d}:{t % 60:02d}")
