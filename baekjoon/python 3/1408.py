# 문제 링크: https://www.acmicpc.net/problem/1408

h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

t = h2 * 3600 + m2 * 60 + s2 - (h1 * 3600 + m1 * 60 + s1)
if t < 0:
    t += 24 * 3600

print(f"{t // 3600:02d}:{(t // 60) % 60:02d}:{t % 60:02d}")
