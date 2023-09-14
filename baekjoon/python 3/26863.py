# 문제 링크: https://www.acmicpc.net/problem/26863

a1, a2, a3, a4, b = (int(input()) for _ in range(5))

a = max(a1, a2, a3, a4) * 4
s = sum([a1, a2, a3, a4])

print(int(a == s or a == s + b))
