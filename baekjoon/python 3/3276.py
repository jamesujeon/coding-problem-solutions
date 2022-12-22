# 문제 링크: https://www.acmicpc.net/problem/3276

N = int(input())

r = c = int(N**.5)
while r * c < N:
    c += 1

print(r, c)
