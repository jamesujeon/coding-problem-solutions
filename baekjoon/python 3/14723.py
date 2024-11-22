# 문제 링크: https://www.acmicpc.net/problem/14723

N = int(input())

i = 0
while i * (i + 1) // 2 < N:
    i += 1

b = N - i * (i - 1) // 2
a = i + 1 - b

print(a, b)
